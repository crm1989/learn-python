# -*- coding: utf-8 -*-
# ============================================================
# Python 第 6 课 · 常用标准库
# ------------------------------------------------------------
# 不学新语法，学 Python 自带的"工具箱"。
# 你已会用 import；这课学的是什么时候用哪个箱子。
# 全部可运行验证。每段先看注释，再看运行结果。
# ============================================================

import random
import datetime
import os
import json


# ------------------------------------------------------------
# 知识点 1：random —— 随机数（游戏、抽题、测试数据必备）
# ------------------------------------------------------------
print("=" * 50)
print("1. random：随机")
print("=" * 50)

print("randint(1,10) 整数 =", random.randint(1, 10))          # 含两端
print("choice 抽一个 =", random.choice(["石头", "剪刀", "布"]))
print("random() 0~1 小数 =", round(random.random(), 3))

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)                                        # 原地打乱！
print("shuffle 洗牌后 =", deck)

print("sample 抽3个不重复 =", random.sample(range(1, 50), 3))

# 第2课的推导式复习：抽5道题
print("抽5道题 =", random.sample(range(1, 101), 5))


# ------------------------------------------------------------
# 知识点 2：datetime —— 时间处理（日志、账单、考勤核心）
# ------------------------------------------------------------
print()
print("=" * 50)
print("2. datetime：时间")
print("=" * 50)

now = datetime.datetime.now()
print("now =", now)
print("年/月/日 =", now.year, now.month, now.day)
print("时/分/秒 =", now.hour, now.minute, now.second)

# 格式化：strftime —— 时间 → 字符串（存文件、显示用）
print("格式化为字符串 =", now.strftime("%Y-%m-%d %H:%M"))

# 反向：strptime —— 字符串 → 时间对象（读文件、解析用户输入）
t = datetime.datetime.strptime("2026-09-30", "%Y-%m-%d") 
print("解析回来的对象 =", t)
print("解析后是星期几 =", t.weekday())   # 0=周一

# 时间差：两个时间相减，得到 timedelta 对象
birth = datetime.datetime(2000, 1, 1)
diff = now - birth
print("出生到现在 =", diff.days, "天")

# 常用格式代码：%Y=年 %m=月 %d=日 %H=时 %M=分 %S=秒


# ------------------------------------------------------------
# 知识点 3：os —— 文件系统操作（整理报表、批量处理必备）
# ------------------------------------------------------------
print()
print("=" * 50)
print("3. os：操作系统")
print("=" * 50)

print("当前工作目录 =", os.getcwd())
print("当前目录文件 =", os.listdir(".")[:5], "...")   # 只显示前5个，避免太长

# 拼路径：别手写 "\\"，用 os.path.join（跨平台自动适配斜杠）
p = os.path.join("data", "2026", "report.csv")
print("os.path.join 拼出的路径 =", p)

# 存在性判断（第3课的"门卫"）
print("这个文件存在吗 =", os.path.exists("12_contacts_file_oop.py"))
print("不存在的路径 =", os.path.exists("不存在的文件夹"))


# ------------------------------------------------------------
# 知识点 4：json —— Python 与外界交换数据的标准格式（AI 篇地基）
# ------------------------------------------------------------
print()
print("=" * 50)
print("4. json：数据交换")
print("=" * 50)

# Python 对象 → JSON 字符串（发给网络、存盘）
student = {"name": "小明", "age": 12, "hobbies": ["足球", "画画"]}
json_str = json.dumps(student, ensure_ascii=False)   # ensure_ascii=False 中文不乱码
print("dumps 变成字符串 =", json_str)

# JSON 字符串 → Python 对象（读网络返回、读文件）
parsed = json.loads(json_str)
print("loads 还原成对象 =", parsed)
print("拿出姓名 =", parsed["name"])

# 文件版的读写（和 txt 一个套路）
with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False)   # 直接写文件

with open("demo.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)                       # 直接读文件
print("从文件读回 =", loaded["hobbies"])


# ------------------------------------------------------------
# 知识点 5：组合实战 —— 用今天学的做一个"账单记录器"
# ------------------------------------------------------------
print()
print("=" * 50)
print("5. 组合实战：账单记录器")
print("=" * 50)

# 场景：每笔账单记录 时间/项目/金额，存成 json，程序重启不丢
BILL_FILE = "bills.json"

def add_bill(item, amount):
    # ① 读旧账单（文件不存在就当空列表）
    bills = json.load(open(BILL_FILE, encoding="utf-8")) if os.path.exists(BILL_FILE) else []
    # ② 加一条新账单
    bills.append({
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "item": item,
        "amount": amount
    })
    # ③ 写回文件
    with open(BILL_FILE, "w", encoding="utf-8") as f:
        json.dump(bills, f, ensure_ascii=False, indent=2)   # indent=2 格式化，人眼可读
    return len(bills)

# 演示：连续记三笔
for item, amount in [("午饭", 25), ("地铁", 4), ("咖啡", 30)]:
    n = add_bill(item, amount)
    print(f"已记录第 {n} 笔：{item} {amount}元")

# 读回来看
with open(BILL_FILE, encoding="utf-8") as f:
    data = json.load(f)
    total = sum(b["amount"] for b in data)   # 第2课推导式：取amount字段求和
    print(f"\n共 {len(data)} 笔，总花费 {total} 元")

print("\n生成的 bills.json 文件已保存在你的项目文件夹里，打开看看长什么样")


# ------------------------------------------------------------
# 总结：什么时候用哪个
# ------------------------------------------------------------
print()
print("=" * 50)
print("【本课速查表】")
print("=" * 50)
print("""
random      游戏/抽题/测试数据 → randint / choice / shuffle / sample
datetime    时间/日志/账单     → now() / strftime / strptime / 时间差
os          文件系统/整理报表  → listdir / path.join / path.exists
json        网络交换/AI API    → dumps / loads / dump / load

四个库组合 = 一个能存数据、能读时间、能联网的完整程序
""")
