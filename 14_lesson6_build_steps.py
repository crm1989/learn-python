# -*- coding: utf-8 -*-
# ============================================================
# 第 6 课 · 分步拆解练习：迷你记账本
# ------------------------------------------------------------
# 目的：证明"组合实战"你也能写——只要一次只写一步。
# 全程不用任何没教过的简写（没有三元表达式，全都用 with）。
#
# 做法：从上到下，每一步只填 1~2 行，填完先别急着往下，
#       文件末尾有"逐步验证"，运行看结果对不对再继续。
# 休眠 CUE 再开始。
# ============================================================

import json
import os
import datetime

LEDGER = "my_ledger.json"


# ------------------------------------------------------------
# 步骤 1：读账本
#   文件在 → 用 json.load 读出列表
#   文件不在 → 返回空列表 []
# （这就是通讯录项目 AddressBook.load 的极简版，你写过）
# ------------------------------------------------------------
def load_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

# ------------------------------------------------------------
# 步骤 2：存账本
#   把整个列表用 json.dump 写回文件（覆盖写 "w"）
#   已帮你写好函数头，你只需要补 with 那两行。
#   参考：with open(LEDGER, "w", encoding="utf-8") as f:
#             json.dump(bills, f, ensure_ascii=False)
# ------------------------------------------------------------
def save_ledger(bills):
    # pass   # ← 删掉 pass，写两行 with 代码
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(bills,f,ensure_ascii=False)

# ------------------------------------------------------------
# 步骤 3：记一笔
#   ① 先读出旧账本（调步骤1的函数）
#   ② append 一个字典，三个键：
#        "time"   → 当前时间字符串，格式 "%Y-%m-%d %H:%M"
#                   提示：datetime.datetime.now().strftime(...)
#        "item"   → 参数 item
#        "amount" → 参数 amount
#   ③ 存回去（调步骤2的函数）
# 每一步都给了注释，你只需在对应注释下补一行
# ------------------------------------------------------------
def add_bill(item, amount):
    # ① 读旧账本，赋值给 bills
    # bills = None    # ← 改成：bills = load_ledger()
    bills = load_ledger() 

    # ② 追加一条记录（这行已写好，读懂即可）
    bills.append({
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "item": item,
        "amount": amount
    })

    # ③ 存回去
    # pass    # ← 写：save_ledger(bills)
    save_ledger(bills)
    

# ------------------------------------------------------------
# 步骤 4：算总花费
#   用推导式把每笔的 amount 取出来，再用 sum() 求和
#   提示：sum(b["amount"] for b in bills)
#   （第2课推导式，你在第6课讲义里见过同款）
# ------------------------------------------------------------
def total_amount(bills):
    # pass    # ← 写：return sum(b["amount"] for b in bills)
    return sum(b["amount"] for b in bills)

# ------------------------------------------------------------
# 主程序（已写好，不要改）
# ------------------------------------------------------------
def main():
    print("迷你记账本")
    while True:
        print("\n1. 记一笔  2. 看汇总  3. 退出")
        choice = input("选择：")
        if choice == "1":
            item = input("项目：").strip()
            amount_text = input("金额：").strip()
            # 第3课复习：用 try/except 防止用户输入非数字
            try:
                amount = int(amount_text)
            except ValueError:
                print("金额必须是整数")
                continue
            if not item:
                print("项目不能为空")
                continue
            add_bill(item, amount)
            print("已记录")
        elif choice == "2":
            bills = load_ledger()
            if not bills:
                print("还没有记录")
            else:
                for b in bills:
                    print(f"{b['time']}  {b['item']}  {b['amount']}元")
                print(f"共 {len(bills)} 笔，合计 {total_amount(bills)} 元")
        elif choice == "3":
            print("再见")
            break
        else:
            print("无效选项")


if __name__ == "__main__":
    main()
