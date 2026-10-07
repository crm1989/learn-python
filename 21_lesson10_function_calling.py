# -*- coding: utf-8 -*-
# ============================================================
# 第 10 课：Function Calling——让 AI 调用你的 Python 函数
# ------------------------------------------------------------
# 核心思想（一句话）：
#   AI 负责"听懂人话、决定调哪个函数、填什么参数"
#   你的代码负责"真正执行函数、把结果还给 AI"
#   AI 拿到结果后再组织成人话回答用户
#
# 流程图：
#   用户："记一笔，午饭花了25"
#     ↓ ①把用户的话发给 AI（附带函数说明书 tools）
#   AI："我要调 add_bill，参数是 type=支出, category=餐饮, amount=25"
#     ↓ ②你的代码解析出函数名和参数 → 真正执行 add_bill(...)
#     ↓ ③把执行结果（"已记录"）再发给 AI
#   AI："好的，已帮你记下：午饭 25 元。"  ← 组织成人话
#
# 注意：AI 只是"说"它想调什么函数，永远不会自己执行——
#       执行权永远在你的代码手里，这就是安全性所在。
#
# 你的 3 个填空：① ② ③（搜 "空" 字）
# 运行：py 21_lesson10_function_calling.py
# ============================================================

import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ZHIPU_API_KEY")
if not API_KEY:
    print("没找到 Key，请先创建 .env 文件")
    raise SystemExit

URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# ============================================================
# 第 1 部分：三个真实的 Python 函数（就是记账本里的！）
#   它们是"干活的人"，AI 只是指挥它们
# ============================================================

LEDGER_FILE = "ai_ledger.json"
BUDGET = 3000


def load_bills():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_bills(bills):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(bills, f, ensure_ascii=False, indent=2)


def add_bill(bill_type, category, amount, note=""):
    """记一笔账。AI 会调用它！"""
    bills = load_bills()
    bills.append({
        "type": bill_type,        # "收入" 或 "支出"
        "category": category,     # 如 餐饮/交通/工资
        "amount": amount,
        "note": note
    })
    save_bills(bills)
    return f"已记录：{bill_type} {category} {amount}元"


def sum_by_type(bill_type):
    """按类型求和。AI 会调用它！"""
    bills = load_bills()
    total = sum(b["amount"] for b in bills if b["type"] == bill_type)
    return f"{bill_type}合计：{total}元（共{len([b for b in bills if b['type'] == bill_type])}笔）"


def list_bills():
    """列出所有账单。AI 会调用它！"""
    bills = load_bills()
    if not bills:
        return "账本是空的"
    lines = [f"{b['type']}|{b['category']}|{b['amount']}元|{b['note']}" for b in bills]
    return "共%d笔：" % len(bills) + "；".join(lines)


# ============================================================
# 第 2 部分：tools——用 JSON 写的"函数说明书"
#   这是给 AI 看的：告诉它有哪些函数可用、参数是什么意思
#   AI 就是根据这份说明书决定"该调谁、怎么填参数"
# ============================================================

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "add_bill",
            "description": "记一笔账。用户说'花了''买了'是支出；'收到''工资'是收入",
            "parameters": {
                "type": "object",
                "properties": {
                    "bill_type": {
                        "type": "string",
                        "description": "账单类型，只能是 收入 或 支出",
                        "enum": ["收入", "支出"]
                    },
                    "category": {
                        "type": "string",
                        "description": "消费类别，如：餐饮/交通/娱乐/工资/理财"
                    },
                    "amount": {
                        "type": "number",
                        "description": "金额，纯数字"
                    },
                    "note": {
                        "type": "string",
                        "description": "备注，一句话说明这笔钱的用途"
                    }
                },
                "required": ["bill_type", "category", "amount"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sum_by_type",
            "description": "统计收入总额或支出总额。用户问'花了多少''收入多少'时调用",
            "parameters": {
                "type": "object",
                "properties": {
                    "bill_type": {
                        "type": "string",
                        "description": "要统计的类型：收入 或 支出",
                        "enum": ["收入", "支出"]
                    }
                },
                "required": ["bill_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_bills",
            "description": "列出账本里全部账单明细。用户问'都有哪些账''账单明细'时调用",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]

# 函数名 → 真函数对象 的对照表
#   AI 返回的是字符串"add_bill"，你得靠这张表找到真正的函数去执行
AVAILABLE_FUNCTIONS = {
    "add_bill": add_bill,
    "sum_by_type": sum_by_type,
    "list_bills": list_bills
}


# ============================================================
# 第 3 部分：和 AI 对话的核心函数
# ============================================================

def chat(messages):
    """发消息给 AI，返回完整响应 JSON（不只是文字）"""
    body = {
        "model": "glm-4-flash",
        "messages": messages,
        "tools": TOOLS            # ← 关键！把函数说明书一并交给 AI
    }
    r = requests.post(URL, headers=HEADERS, json=body, timeout=60)
    r.raise_for_status()
    return r.json()


def run_once(user_input, history):
    """
    处理一轮对话，返回 AI 最终的回复。
    内部完成"AI想调函数 → 你执行 → 结果还给AI → AI说人话"的完整循环。
    """
    history.append({"role": "user", "content": user_input})

    # 第 1 次调用 AI
    resp = chat(history)
    msg = resp["choices"][0]["message"]

    # ============ 情况 A：AI 决定调用函数 ============
    if msg.get("tool_calls"):
        history.append(msg)   # 把 AI 的"调用决定"记进历史（协议要求）

        for tool_call in msg["tool_calls"]:
            fn_name = tool_call["function"]["name"]         # 例如 "add_bill"
            fn_args = json.loads(tool_call["function"]["arguments"])  # 参数字典

            print(f"   [AI 正在调用函数：{fn_name}，参数={fn_args}]")

            # 空 ①：从 AVAILABLE_FUNCTIONS 对照表里取出真正的函数
            #   提示：函数 = AVAILABLE_FUNCTIONS[?]
            函数 = None  # ← 删掉这行，写 1 行


            # 空 ②：带着参数执行函数，拿到结果字符串
            #   提示：**fn_args 会把字典拆成关键字参数
            #        等价于 add_bill(bill_type="支出", category="餐饮", amount=25)
            #        如果字典是空的（list_bills 没参数），就直接 函数()
            if fn_args:
                result = None  # ← 删掉，改成：result = 函数(**fn_args)
            else:
                result = 函数()


            # 空 ③：把执行结果按协议格式追加进 history
            #   协议规定：role 固定为 "tool"，还要带上这次调用的 id
            #   提示：history.append({
            #            "role": "tool",
            #            "tool_call_id": tool_call["id"],
            #            "content": <执行结果>
            #        })
            pass  # ← 删掉，写 append（多行字典）


        # 第 2 次调用 AI：它看到函数结果，会组织成人话回答
        resp2 = chat(history)
        reply = resp2["choices"][0]["message"]["content"]
        history.append({"role": "assistant", "content": reply})
        return reply

    # ============ 情况 B：AI 直接回答（没调函数） ============
    reply = msg.get("content") or ""
    history.append({"role": "assistant", "content": reply})
    return reply


# ============================================================
# 第 4 部分：主程序（已写好）
# ============================================================

def main():
    print("=" * 46)
    print("  AI 智能记账助手（自然语言记账，输入 退出 结束）")
    print("=" * 46)
    print("试试说：记一笔，午饭花了25元 / 这个月支出多少 / 看看账单")
    print()

    system_msg = {
        "role": "system",
        "content": "你是一个简洁的记账助手。用户让你记账时必须调用函数，不要自己编造记账结果。"
    }
    history = [system_msg]

    while True:
        user_input = input("我：").strip()
        if user_input in ["退出", "quit", "exit"]:
            print("再见！")
            break
        if not user_input:
            continue
        try:
            reply = run_once(user_input, history)
        except requests.RequestException as e:
            print("网络出错：", e)
            history.pop()
            continue
        print("AI：", reply)
        print()


if __name__ == "__main__":
    main()
