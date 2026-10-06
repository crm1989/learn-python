# -*- coding: utf-8 -*-
# ============================================================
# AI 应用篇 · 课程项目 1：命令行聊天机器人
# ------------------------------------------------------------
# 这是你第一个真正"能用"的 AI 程序：
#   - 可以无限连聊（while True，第1课）
#   - AI 有记忆（history 列表，第9课知识点4/6）
#   - AI 有人设（system prompt，第9课知识点5）
#   - 网络出错不会崩（try/except，第3/8课）
#
# 运行：py 20_chatbot.py
# 退出：输入 退出 / quit / exit，或按 Ctrl+C
#
# 你要填 4 个空（都在下面标了 ①②③④）
# ============================================================

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

# 人设——改这一段就能改变整个机器人的性格！
# 以后做儿童辅导机器人，规则就写在这里（不许闲聊/只提问不给答案...）
SYSTEM_PROMPT = "你是一个友好、耐心的聊天伙伴，用简洁的中文回答。"

def ask(messages):
    """把完整对话历史发给大模型，返回 AI 的文字回复"""
    body = {
        "model": "glm-4-flash",
        "messages": messages
    }
    r = requests.post(URL, headers=HEADERS, json=body, timeout=60)
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"]["content"]
    # 空 ①：从 data 里取出 AI 的回复文字
    #   响应结构（讲义知识点3）：
    #   data = {"choices": [{"message": {"content": "AI说的话"}}], ...}
    #   提示：data["choices"][?]["message"][?]
    #   把结果 return 出去
    pass  # ← 删掉 pass，写 1 行 return


def main():
    print("=" * 40)
    print("  我的聊天机器人（输入 退出 结束对话）")
    print("=" * 40)

    # 对话历史：一开机就把人设放进去
    history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        user_input = input("\n我：").strip()

        # 空 ②：退出条件
        #   如果用户输入的是 "退出"、"quit"、"exit" 中的任意一个
        #   就打印"再见"并 break 跳出循环
        #   提示：if user_input in ["退出", "quit", "exit"]:
        # pass  # ← 删掉 pass，写 3 行（if / print / break）
        if user_input in ["退出", "quit", "exit"]:
            print("再见")
            break

        if not user_input:
            continue   # 输入空行不发送，重新等输入

        # 空 ③：把用户这句话加进历史
        #   回忆讲义第154行：
        #   history.append({"role": "user", "content": 用户的话})
        # pass  # ← 删掉 pass，写 1 行 append
        history.append({"role": "user", "content": user_input})

        # 发给 AI（网络异常时提示而不是崩溃）
        try:
            reply = ask(history)
        except requests.RequestException as e:
            print("网络出错了：", e)
            print("（对话历史已保留，可以重试）")
            # 把刚才那句没发成功的用户消息撤掉，避免历史错乱
            history.pop()
            continue

        if reply is None:
            print("AI 没有返回内容，请重试")
            history.pop()
            continue

        print("AI：", reply)

        # 空 ④：把 AI 的回复也加进历史
        #   回忆讲义第158行：
        #   history.append({"role": "assistant", "content": AI的话})
        #   不写这一步，AI 下一轮就会"失忆"！
        # pass  # ← 删掉 pass，写 1 行 append
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
