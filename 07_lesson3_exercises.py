# -*- coding: utf-8 -*-
# ============================================================
# Python 第三课 · 综合测试卷
# 考察重点：try/except 精准捕获、while+try 输入校验、
#           with open 三种模式、strip+split 读写表格数据
# 复习重点：第 2 课遗留点（打擂台记姓名、推导式只取字段、切片存变量）
#
# 考试规则（和前两课相同）：
#   第一部分：先不要运行！先读代码，写下你预测的结果，
#             全部写完后再运行对照（运行： py 07_lesson3_exercises.py）
#   第二部分：找出错误，先说出"错在哪、怎么改"，再动手改
#   第三部分：动手写代码。做题前记得休眠 CUE（右下角 CUE 图标 → 休眠）
# ============================================================


from re import split
from shlex import join


print("【第一部分】看代码，写结果")
print("-" * 40)

# 第 1 题：会打印哪几行？try 里哪行能执行到？
try:
    print("A")
    x = 10 / 0
    print("B")
except ZeroDivisionError:
    print("C")
print("D")

# 第 2 题：两个结果分别是什么？
def parse(text):
    try:
        return int(text)
    except ValueError:
        return -1

print("第2题：", parse("42"), parse("abc"))

# 第 3 题：会打印什么？（注意 except 捕获的是哪种错误）
try:
    d = {"a": 1}
    print(d["b"])
except KeyError:
    print("键不存在")
except IndexError:
    print("下标越界")

# 第 4 题：写完文件后读取，print 出什么？
with open("test_q4.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\n30\n")

with open("test_q4.txt", "r", encoding="utf-8") as f:
    total = 0
    for line in f:
        total = total + int(line.strip())
print("第4题：", total)

# 第 5 题：追加模式后文件里有几行？读出来列表多长？
with open("test_q5.txt", "w", encoding="utf-8") as f:
    f.write("apple\n")
with open("test_q5.txt", "a", encoding="utf-8") as f:
    f.write("banana\n")

with open("test_q5.txt", "r", encoding="utf-8") as f:
    fruits = [line.strip() for line in f]
print("第5题：", fruits, len(fruits))

# 第 6 题（第 2 课复习）：切片结果是什么？
s = "2026-09-28"
print("第6题：", s[:4], s[5:7], s[-2:])

# 第 7 题（第 2 课复习）：列表装字典，取什么？
students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
]
print("第7题：", students[1]["name"], students[0]["score"])


print()
print("【第二部分】找出错误")
print("-" * 40)
print("以下 4 段代码都有问题。先说出错因和改法，再动手改。")
print("提示：有的会报错，有的不报错但结果不对！")

# 第 8 题（会报错）：
#
# f = open("data.txt", "w", encoding="utf-8")
# f.write("内容")
# 上面两行代码有什么隐患？（提示：和文件关闭有关）

# 第 9 题（不报错，但 except 写法有问题）：
#
# try:
#     age = int(input("年龄："))
# except:
#     print("出错了")  是不是没有指定异常？
# 这样写能运行，但有什么不好？（提示：它会把不该藏的 bug 也藏起来）

# 第 10 题（会报 KeyError，但读文件前应该先做什么？）：
#
# with open("maybe_missing.txt", "r", encoding="utf-8") as f:
#     print(f.read())  先做os的exsit检查？

# 第 11 题（第 2 课复习 · 推导式写法错误）：
#
# names = [for s in students if s["score"] >= 80 s["name"]]
# 这样？ names = [s["name"] for s in students if s["score"] >= 80 ]


print()
print("【第三部分】动手写代码")
print("-" * 40)

# 第 12 题（输入校验）：写一个函数 safe_input_int
# 要求：不断让用户输入，直到输入的是合法整数才返回该整数
#       输入非整数时提示"不是整数，请重输"，然后继续等待
#       用 while True + try/except ValueError 实现
# 本文件演示时不等待键盘，函数定义好即可（可以取消注释亲手试）
def safe_input_int(prompt):
    while True:
        inputstr = input("输入整数:")
        try:
            return int(inputstr)
        except ValueError:
            print("不是整数，请重输")
a = 0
rst = safe_input_int(a)
print(rst)

# 第 13 题（文件读写综合）：把列表写成文件再读回
# 要求：
# 1) 把 products 列表写入 products.txt，每行格式 "名称,价格"
# 2) 再从文件读回，用 split(",") 还原成字典，存入 loaded_products
# 3) 价格读回时用 int() 转成数字
products = [
    {"name": "苹果", "price": 5},
    {"name": "香蕉", "price": 3},
]
# 在下面写你的代码：
with open("products.txt", "w",encoding="utf-8") as f:
    for p in products:
        line = f"{p["name"]},{p["price"]}\n"
        f.write(line)
loaded_products = []
with open("products.txt", "r",encoding="utf-8") as f:
    for line in f:
        sp = line.split(",")
        loaded_products.append({"name": sp[0] , "price": int(sp[1])})

print(loaded_products)

# 第 14 题（第 2 课复习 · 打擂台记姓名）：
# 用 for 循环遍历 students2，找出分数最高的学生姓名，存入 top_name
# 注意：题目要的是姓名，不是分数！分数刷新时姓名要一起刷新
students2 = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 72},
]
# 在下面写你的代码：
maxs = 0
for i in students2:
    if i["score"] > maxs:
        maxs = i["score"]
        highname = i["name"]
print(highname)

# 第 15 题（第 2 课复习 · 推导式只取字段）：
# 用一个列表推导式，收集 students2 中所有 80 分以上学生的姓名
# 注意：收集的是姓名字符串，不是整个字典！存入 passed_names
# 在下面写你的代码：
passed_names = [ n["name"] for n in students if int(n["score"]) >= 80]
print(passed_names)

# 挑战题（综合 · 文件版单词统计）：
# 把下面的句子写入 words.txt（每行一个单词），再读回统计每个单词出现次数
# 结果存入字典 word_counts 并打印
# 期望结果：{'to': 2, 'be': 2, 'or': 1, 'not': 1}
sentence = "to be or not to be"
# 提示：先 split 得到单词列表，逐行 write 到文件（每行一个词+\n）
#       再逐行 read 回来，strip 后用第一课"水果统计"思路计数
# 在下面写你的代码：
word_counts = {}
with open("words.txt","r",encoding="utf-8") as f:
    for l in f: 
        moto = l.split(" ")
        for n in moto:
            if n in word_counts:
                word_counts[n] += 1
            else:
                word_counts[n] = 1
print(word_counts)


# ============================================================
# 自测区：第三部分写完后，把下面的注释逐个取消，运行本文件
# 不报错 = 全部通过
# ============================================================
# assert safe_input_int.__doc__ is None or True   # 函数已定义即可
# assert loaded_products == [{"name": "苹果", "price": 5}, {"name": "香蕉", "price": 3}]
# assert top_name == "小红"
# assert passed_names == ["小明", "小红"]
# assert word_counts == {"to": 2, "be": 2, "or": 1, "not": 1}
