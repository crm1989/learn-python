# -*- coding: utf-8 -*-
# ============================================================
# Python 第二课 · 综合测试卷
# 考察重点：切片、字符串方法、列表推导式、嵌套结构（列表装字典）
#
# 考试规则（和第一课相同）：
#   第一部分：先不要运行！先读代码，写下你预测的结果，
#             全部写完后再运行对照（运行： py 05_lesson2_exercises.py）
#   第二部分：找出错误，先说出"错在哪、怎么改"，再动手改
#   第三部分：动手写代码。做题前记得休眠 CUE（右下角 CUE 图标 → 休眠）
# ============================================================



print("【第一部分】看代码，写结果")
print("-" * 40)

# 第 1 题：三个结果分别是什么？
s = "Python"
print("第1题：", s[1:3], s[-2:], s[::-1])

# 第 2 题：三个结果分别是什么？（切片规则对列表也一样）
nums = [5, 10, 15, 20, 25, 30]
print("第2题：", nums[2:], nums[:3], nums[::2])

# 第 3 题：四个结果分别是什么？（注意 len 数的是几个字符）
text = "  hello world  "
t = text.strip()
print("第3题：", len(text), len(t), t.upper(), t.replace("world", "python"))

# 第 4 题：三个结果分别是什么？
date = "2026-09-28"
parts = date.split("-")
print("第4题：", parts, len(parts), "/".join(parts))

# 第 5 题：打印什么？
result = [n * 2 for n in range(1, 5)]
print("第5题：", result)

# 第 6 题：打印什么？
result = [n for n in range(1, 10) if n % 2 == 1]
print("第6题：", result)

# 第 7 题：三个结果分别是什么？（列表装字典，先下标后键）
books = [
    {"title": "三体", "price": 45},
    {"title": "活着", "price": 30},
]
print("第7题：", books[0]["title"], books[1]["price"], len(books))

# 第 8 题：会打印哪几行？（enumerate 的编号从几开始？）
for i, name in enumerate(["a", "b", "c"]):
    print("第8题：", i, name)


print()
print("【第二部分】找出错误")
print("-" * 40)
print("以下 4 段代码都有问题。先说出错因和改法，再取消注释验证。")
print("提示：有的会直接报错，有的不报错但结果是错的（更隐蔽）！")

# 第 9 题：
#
s = "hello"
# s[0] = "H"
s = s.replace("h","H")
print(s)

# 第 10 题（不报错，但 print 出来的不是你想要的）：
#
nums = [3, 1, 2]
nums.sort()
print("排序结果：", sorted(nums))
print("排序结果：", sorted(nums,reverse=True))

# 第 11 题：
#
student = {"name": "小明", "score": 88}
# print(student["age"])
print(student["score"])

# 第 12 题（推导式的写法出了问题）：
#
# result = [for n in range(3) n * 2]
result = [n * 2 for n in range(3)]
print(result)


print()
print("【第三部分】动手写代码")
print("-" * 40)

# 第 13 题（切片实战）：从身份证号提取信息
# 已知：身份证下标 6 到 13 这 8 位是出生日期；
#       下标 -2（倒数第 2 位）是性别码：奇数=男，偶数=女
id_number = "352201198908290032"
# 要求：
# 1) 用切片取出生日 8 位，存入变量 birthday 并打印
# 2) 判断性别：注意 id_number[-2] 拿到的是字符串，要 int() 转数字再判断奇偶，
#    结果存入变量 gender（值为 "男" 或 "女"）并打印
# 在下面写你的代码：
if int(id_number[-2]) % 2 != 0:
    gender = "男"
else:
    gender = "女"
print("出生日期:",id_number[6:14],"性别",gender)

# 第 14 题（推导式实战）：清洗数据
# raw 里有的词带多余空格，有的甚至是纯空格或空字符串
# 要求：用一个列表推导式得到：每个词去掉两端空格，并且丢掉空的
# 期望结果：['apple', 'banana', 'cherry']，结果存入变量 cleaned
raw = ["  apple ", "banana", "  ", "cherry", ""]
# 在下面写你的代码：
cleaned = [ n.strip() for n in raw if n.strip() != ""  ]
print(cleaned)

# 第 15 题（嵌套结构实战）：学生成绩管理
students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 72},
    {"name": "小李", "score": 60},
]


# 要求：
# 1) 用 for 循环打印每个人，格式如： 小明：88分
# 2) 不用 max()，用"打擂台"找出最高分学生的姓名，
#    存入变量 top_name 并打印（提示：先假设第一个学生分数最高）
# 3) 用一个列表推导式收集所有 80 分以上学生的姓名，存入变量 passed 并打印
# 在下面写你的代码：
highscore = students[0]["score"]
for stu in students:
    if stu["score"] > highscore:
        highscore = stu["score"]
    print(f"{stu["name"]}:{stu["score"]}")
print("学生分数最高:",highscore)
passed = [n for n in students if int(n["score"]) >= 80]
print(passed)

# 挑战题（选做，衔接第一课）：单词统计
# 把句子切分成单词，统计每个单词出现次数，结果存入字典 counts 并打印
# 期望结果：{'to': 2, 'be': 2, 'or': 1, 'not': 1}
sentence = "to be or not to be"
# 提示：先用 .split() 切开，再用第一课"水果统计"的思路
# 在下面写你的代码：
counts = sentence.split(" ")
print(counts)
cntlist = {}
for word in counts:
    if word in cntlist:
        cntlist[word] += 1
    else:
        cntlist[word] = 1
print(cntlist)

# ============================================================
# 自测区：第三部分写完后，把下面的注释逐个取消，运行本文件
# 不报错 = 全部通过
# ============================================================
# assert birthday == "20050101"
# assert gender == "男"
# assert cleaned == ["apple", "banana", "cherry"]
# assert top_name == "小红"
# assert passed == ["小明", "小红"]
# assert counts == {"to": 2, "be": 2, "or": 1, "not": 1}
