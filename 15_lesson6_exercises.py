# -*- coding: utf-8 -*-
# ============================================================
# 第 6 课测试卷 · 常用标准库（random / datetime / os / json）
# ------------------------------------------------------------
# 规则：第一部分先写预测再运行；卡壳超过5分钟说"提示第X题"。
# 做题前：休眠 CUE；每填完一块就 Ctrl+S！
# 自测区：全部做完后取消注释，运行无输出 = 全对
# ============================================================

import random
import datetime
import os
import json

print("【第一部分】看代码，写结果")
print("-" * 40)

# --- 第 1 题（random 基础）---
# nums = [1, 2, 3, 4, 5]
# result = random.choice(nums)
# print(result)          # 写出可能的取值范围：____
# random.shuffle(nums)
# print(nums[0])         # 写出可能的取值：____
# x = random.randint(1, 3)
# print(x)               # 写出可能的取值：____

# --- 第 2 题（datetime 格式化）---
now = datetime.datetime(2026, 10, 1, 9, 5, 8)
print(now.strftime("%Y/%m/%d"))      # 输出：____
print(now.strftime("%H:%M"))         # 输出：____
print(now.year, now.month)           # 输出：____

# --- 第 3 题（datetime 解析 + 时间差）---
t1 = datetime.datetime.strptime("2026-10-01", "%Y-%m-%d")
t2 = datetime.datetime(2026, 12, 25)
print((t2 - t1).days)                # 输出：____
print(t1.weekday())                  # 2026-10-01 是周四，输出：____

# --- 第 4 题（os）---
print(os.path.exists("13_lesson6_stdlib.py"))   # 输出：____
p = os.path.join("data", "bill.json")
print(p)                             # 输出：____（注意分隔符）

# --- 第 5 题（json 来回转换）---
student = {"name": "小明", "scores": [90, 80]}
s = json.dumps(student, ensure_ascii=False)
print(type(s).__name__)              # 输出：____
back = json.loads(s)
print(back["scores"][1])             # 输出：____

# --- 第 6 题（复习·第2课推导式）---
bills = [{"item": "午饭", "amount": 25}, {"item": "地铁", "amount": 4}, {"item": "书", "amount": 50}]
print(sum(b["amount"] for b in bills))          # 输出：____
print([b["item"] for b in bills if b["amount"] > 10])   # 输出：____

# --- 第 7 题（复习·第4课 sort/sorted 陷阱同款）---
data = [3, 1, 2]
result = data.sort()
print(result)                        # 输出：____（想想 sort 返回什么）
print(sorted(data))                  # 输出：____

print()
print("【第二部分】找出错误（先说错因，再改正）")
print("-" * 40)

# --- 第 8 题：想把文件里的数据读成 Python 对象，哪里错了？---
with open("bills.json","r",encoding="utf-8") as f:
    data = json.load(f)
print(data)

# --- 第 9 题：想把字符串"变成"时间对象，哪里错了？---
t = datetime.datetime.strptime("2026-10-01", "%Y-%m-%d")
print(t)

# --- 第 10 题：洗牌后为什么是 None？和第7题是什么关系？---
cards = [1, 2, 3]
random.shuffle(cards)
print(cards)

# --- 第 11 题：读取成绩文件，可能在哪一步崩？（数据文件不存在时）---
if os.path.exists("scores.json") :
    with open("scores.json", "r", encoding="utf-8") as f:
        scores = json.load(f)
    print(scores[0])

print()
print("【第三部分】动手写代码")
print("-" * 40)

# --- 第 12 题：掷骰子函数 ---
# 要求：写函数 roll_dice(times)，掷 times 次骰子（1~6），
#       返回结果列表。变量名必须叫 rolls。
# 例：roll_dice(3) 可能返回 [5, 2, 6]
# rolls = None   # ← 写好后取消这行注释改成真正调用
# assert len(rolls) == 3 and all(1 <= r <= 6 for r in rolls)
def roll_dice(times):
    rolls = []
    for i in range(times):
        rolls.append(random.randint(1,6))
    return rolls

print(roll_dice(5))

# --- 第 13 题：倒计时函数 ---
# 要求：写函数 days_until(year, month, day)，
#       返回"今天"距离指定日期还有多少天（整数）。
#       过去了返回负数也算对。变量名必须叫 left。
# 提示：今天 = datetime.datetime.now()；目标 = datetime.datetime(year, month, day)
# left = None
# assert isinstance(left, int)
def days_until(year, month, day):
    left = (datetime.datetime(year, month, day) - datetime.datetime.now()).days
    return left

print(days_until(2026,12,15))

# --- 第 14 题：JSON 存取函数对 ---
# 要求：写两个函数
#   save_books(books)：把图书列表（字典的列表）存入 books.json
#   load_books()：读回该文件并返回列表；文件不存在返回 []
# 注意中文！注意路径门卫！

def save_books(books):
    with open("books.json","w",encoding="utf-8") as f:
        json.dump(books,f, ensure_ascii=False)
def load_books():
    if os.path.exists("books.json"):
        with open("books.json","r",encoding="utf-8") as f:
            return json.load(f)
    else:
        return []


books = [{"title": "三体", "price": 45}]
save_books(books)
assert load_books() == books
assert load_books.__doc__ is not None or True   # 这行只是占位


# --- 第 15 题（综合）：消费汇总器 ---
# bills.json 已存在（第6课讲义生成的，也可以自己造）。
# 要求：写函数 sum_by_date(filename)，
#   读取 json 文件（列表，每项含 "time" 和 "amount"），
#   返回总金额（所有 amount 之和）。变量名必须叫 total。
#   文件不存在时返回 0。
# total = None
# assert total >= 0
def sum_by_date(filename):
    amount = 0
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as f:
            for am in json.load(f):
                amount += am["amount"]
            return amount
    else:
        return 0

print(f"amount:{sum_by_date("bills.json")}")

# --- 挑战题：随机点名器 ---
# students.json 里存姓名列表（自己先造一个文件：["小明","小红","小刚","小丽"]）
# 写函数 pick(n)：
#   1) 从 students.json 读名单
#   2) 随机抽出 n 个【不重复】的名字
#   3) 每抽一次，往 picked_log.txt 追加一行"时间,名字"（用 strftime）
#   4) 返回抽中的列表，变量名必须叫 winners
# winners = None
# assert len(winners) == 2

# stu = ["小明","小红","小刚","小丽"]
# def save_stu(st):
#     with open("students.json","w",encoding="utf-8") as f:
#         json.dump(st,f, ensure_ascii=False)
# save_stu(stu)

# def pick(n):
#     if os.path.exists("students.json"):
#         winners = {}
#         with open("students.json","r",encoding="utf-8") as f:
#             stulist = json.load(f)
#             if n <= len(stulist):
#                 for i in range(0,n):
#                     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     sdx = random.randint(0,len(stulist)-1)
#                     winners[now] = stulist[sdx]
#                     del stulist[sdx]
#             else:
#                 print("n的值比文件内的名字数多")
#         return winners
#     else:
#         return 0
def pick(n):
    if os.path.exists("students.json"):
        winners = []
        with open("students.json","r",encoding="utf-8") as f:
            stulist = json.load(f)
        
        if n <= len(stulist):
            picked_names = random.sample(stulist, n)
            for name in picked_names:
                now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # 追加写入日志
                with open("picked_log.txt","a",encoding="utf-8") as log_f:
                    log_f.write(f"{now_str},{name}\n")
                winners.append(name)
        else:
            print("n的值比文件内的名字数多")
        return winners
    else:
        print("students.json不存在")
        return []

print(pick(3))

print()
print("【自测区】全部做完后取消下面注释运行，无输出=全对")
print("-" * 40)
# assert isinstance(rolls, list) and len(rolls) == 3
# assert isinstance(left, int)
# assert load_books() == [{"title": "三体", "price": 45}]
# assert isinstance(total, int) and total >= 0
# assert isinstance(winners, list)
print("本文件当前只是题目展示（预测区已注释），完成后再取消注释")
