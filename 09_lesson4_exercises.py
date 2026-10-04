# -*- coding: utf-8 -*-
# ============================================================
# Python 第 4 课 · 综合测试卷
# 考察重点：默认参数、可变默认参数的坑、多返回值、*args、
#           作用域、lambda + sorted 排序、模块
# 复习重点：函数内使用形参、严格按要求命名、选对数据源、
#           文件读写完整步骤（写入 + strip 读取）
#
# 考试规则：
#   第一部分：先不要运行！读代码写下预测结果，全部写完再运行
#             （运行： py 09_lesson4_exercises.py）
#   第二部分：找错误，先说"错在哪、怎么改"，再动手
#   第三部分：动手写。做题前休眠 CUE（右下角 CUE 图标 → 休眠）
# ============================================================


print("【第一部分】看代码，写结果")
print("-" * 40)

# 第 1 题：三次调用分别打印什么？
def power(base, exp=2):
    return base ** exp

print("第1题：", power(3), power(3, 3), power(exp=1, base=5))

# 第 2 题（重点坑！）：两次调用分别打印什么？
def add_tag(item, tags=[]):
    tags.append(item)
    return tags

print("第2题：", add_tag("新闻"))
print("第2题：", add_tag("体育"))

# 第 3 题：三个变量分别是什么？
def swap(a, b):
    return b, a

x, y = swap(10, 20)
only = swap(10, 20)
print("第3题：", x, y, only)

# 第 4 题：两个结果分别是什么？
def join_all(sep, *parts):
    return sep.join(parts)

print("第4题：", join_all("-", "2026", "09", "29"))
print("第4题：", join_all(" ", "a", "b"))

# 第 5 题：函数内外各打印什么？最终的 n 是几？
n = 100

def test():
    n = 5
    print("函数内：", n)

test()
print("第5题函数外：", n)

# 第 6 题：排序后的姓名顺序是什么？
goods = [
    {"name": "铅笔", "price": 2},
    {"name": "书包", "price": 80},
    {"name": "橡皮", "price": 1},
]
cheap_first = sorted(goods, key=lambda g: g["price"])
print("第6题：", [g["name"] for g in cheap_first])

# 第 7 题（模块）：打印什么？
import math
print("第7题：", math.floor(3.9), type(math.pi).__name__)


print()
print("【第二部分】找出错误")
print("-" * 40)
print("以下 4 段代码都有问题。先说出错因和改法，再动手改。")

# 第 8 题（可变默认参数坑，请改成正确写法）：
#
def record(name, history=None):
    if history is None:
        history = []
    history.append(name)
    return history

# 第 9 题（作用域：作者本想修改全局余额，结果没生效）：
#
balance = 100
def spend(amount,balance):
    balance = balance - amount
    print("剩余：", balance)
spend(30,balance)

# 第 10 题（想按分数从高到低排，结果报错或不对）：
#
players = [{"name": "甲", "score": 70}, {"name": "乙", "score": 90}]
result = sorted(players, key=lambda p: p["score"], reverse=True)

# 第 11 题（第 3 课复习 · 文件读取漏了一步，导致键带换行符）：
#
# counts = {}
# with open("words.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         word = line.strip()            # ← 这行少了什么处理？
#         counts[word] = counts.get(word, 0) + 1


print()
print("【第三部分】动手写代码")
print("-" * 40)

# 第 12 题（默认参数 + 形参使用，第 3 课复习点）：
# 写一个函数 make_greeting(name, title="同学")，
# 返回 "XX同学你好" 这样的字符串；传入 title 时用传入的。
# 注意：函数体里只能用形参 name 和 title，不能写死文字以外的东西。
def make_greeting(name, title="同学"):
    return f"{name}{title}你好" # 在这里写代码（用 return 返回，不要 print）

# 第 13 题（多返回值）：写一个函数 analyze(nums)
# 一次返回 3 个值：总和、最大值、最小值（用逗号隔开 return）
# 接收时解包到 s, hi, lo 三个变量并打印
def analyze(nums):
    return  sum(nums),max(nums),min(nums)  # 在这里写代码（可以直接用 sum/max/min）

data = [4, 1, 9, 3]
# 在下面调用 analyze 并解包打印：
s,hi,lo = analyze(data)
print(s,hi,lo)

# 第 14 题（lambda 排序 + 嵌套结构，第 2 课复习点）：
# 对下面 members 按年龄 age 从大到小排序，结果存入 members_sorted
# 然后用推导式只收集排序后所有人的【姓名】，存入 members_names
# 注意：① 数据源是 members ② 变量名必须用题目指定的两个
# ③ 字典里取值用 ["age"]，不能用 .age（那是第 10 题的错法）
members = [
    {"name": "小明", "age": 15},
    {"name": "老王", "age": 40},
    {"name": "小红", "age": 22},
]
# 在下面写代码：
members_sorted = sorted(members,key=lambda s:s["age"],reverse=True)
members_names = [n["name"]  for n in members_sorted ]
print(members_sorted)
print(members_names)

# 第 15 题（第 3 课复习 · 文件读写完整流程）：
# 1) 把 todos 列表写入 todo.txt，每行一个事项（记得加 \n）
# 2) 再从文件读回，【每行先 strip】，收集成新列表 todo_loaded
# 注意：变量名必须是 todo_loaded；写入和读取两步都要写，不能省略
todos = ["买菜", "写作业", "运动"]
# 在下面写代码：
with open("todo.txt","w",encoding="utf-8") as f:
    for a in todos:
        f.write(f"{a}""\n""")

todo_loaded = []
with open("todo.txt","r",encoding="utf-8") as g:
    for b in g:
        todo_loaded.append(b.strip())

print(todo_loaded)

# 挑战题（综合）：带安全默认参数的统计函数
# 写函数 add_score(student, name, score)：
#   student 是形如 {"scores": [...]} 的字典（注意不是列表！）
#   把 score 追加到 student["scores"]，然后返回该列表的平均值
# 再写函数 make_student(name)：返回一个全新学生字典
#   {"name": name, "scores": []}
# 然后创建两个学生分别 add_score，验证他们的 scores 互不影响
# （这题在检验知识点3：可变对象必须每次新建，不能共享）
# 在下面写代码：

def make_student(name):
    return {"name": name , "scores": []}

def add_score(student, score):
    student["scores"].append(score)
    return sum(student["scores"]) / len(student["scores"])

a = make_student( "小明" )
b = make_student( "小红" ) 
print (add_score(a,90)) # 90.0 
print (add_score(a, 80 )) # 85.0（小明的平均） 
print (add_score(b, 70 )) # 70.0（如果这里变成 80，就说明串号了！） 
print (a[ "scores" ], b[ "scores" ])



# ============================================================
# 自测区：写完后取消注释运行，没有任何输出 = 全部通过
# ============================================================
assert make_greeting("小明") == "小明同学你好"
assert make_greeting("王老师", title="老师") == "王老师老师你好"
assert (s, hi, lo) == (17, 9, 1)
assert members_names == ["老王", "小红", "小明"]
assert todo_loaded == ["买菜", "写作业", "运动"]
