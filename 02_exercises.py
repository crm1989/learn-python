# -*- coding: utf-8 -*-
# ============================================================
# Python 第一课 · 综合测试卷
# 考试规则（很重要）：
#   第一部分：先不要运行！先读代码，在纸上或聊天里写下你预测的结果，
#             全部写完后再运行本文件对照（直接运行：py 02_exercises.py）
#   第二部分：找出错误，先口头说出“错在哪、怎么改”，再动手改
#   第三部分：在指定位置写出你自己的代码，写完用自测语句验证
# 做完后把你的答案发给我，我来逐题批改、讲解
# ============================================================


print("【第一部分】看代码，写结果")
print("-" * 40)

# 第 1 题：打印什么？
x = 10
x = x + 5
print("第1题：", x)

# 第 2 题：三个结果分别是什么？
print("第2题：", 17 // 5, 17 % 5, 2 ** 4)

# 第 3 题：两行 print 分别输出什么？（注意类型！）
a = "3"
b = "5"
print("第3题第一行：", a + b)
print("第3题第二行：", int(a) + int(b))

# 第 4 题：打印什么？
total = 0
for i in range(1, 5):
    total = total + i
print("第4题：", total)

# 第 5 题：打印什么？
nums = [10, 20, 30]
nums.append(40)
print("第5题：", len(nums), nums[1])

# 第 6 题：两行分别打印什么？
info = {"name": "小刚", "age": 22}
print("第6题第一行：", info["age"])
info["city"] = "广州"
print("第6题第二行：", len(info))

# 第 7 题：打印什么？
n = 7
if n % 2 == 0:
    print("第7题：偶数")
else:
    print("第7题：奇数")

# 第 8 题：会打印哪些数字？（小心 continue 的执行顺序）
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue
    print("第8题：", i)

# 第 9 题：两个 print 分别是什么？
print("第9题第一行：", 3 > 2 and 5 > 10)
print("第9题第二行：", not (1 == 1))

# 第 10 题：打印什么？
def mystery(n):
    return n * n + 1
print("第10题：", mystery(4))


print()
print("【第二部分】找出错误")
print("-" * 40)
print("以下 4 段代码都有问题。请先不要取消注释，")
print("先说出错因和改法，确认理解后再取消注释验证（会报错）")

# 第 11 题（语法错误）：
#
# if 5 > 3:
#     print("对")

# 第 12 题（类型错误）：
#
# age = input("请输入年龄：")
# print(int(age) + 1)

# 第 13 题（运行时错误）：
#
# scores = [90, 80, 70,50]
# print(scores[3])

# 第 14 题（语法错误）：
#
name = "小明"
print(name)


print()
print("【第三部分】动手写代码")
print("-" * 40)

# 第 15 题：用 for 循环计算 1 到 100 所有整数的和并打印（正确结果是 5050）
# 在下面写你的代码：
total = 0
for i in range(1,101):
    total += i 
print(total)   


# 第 16 题：写一个函数 check(n)，
#   如果 n 是偶数，返回字符串 "偶数"；否则返回 "奇数"。
# 提示：用 n % 2 判断，函数里用 return，不要用 print
def check(n):
    # pass  # 删掉这行，写你自己的代码
    if n % 2 == 0:
        return "偶数"
    else:
        return "奇数"

# 第 17 题：不用 max() 函数，用循环找出下面列表中的最大值并打印
numbers = [12, 7, 9, 20, 3, 15]
# 在下面写你的代码：
max_num = 0
for c in numbers:
    if c > max_num:
        max_num = c
print(max_num)

# 第 18 题（综合题）：统计下面列表中每种水果出现的次数，结果放进字典并打印
# 期望结果类似：{'苹果': 3, '香蕉': 2, '橘子': 1}
fruits = ["苹果", "香蕉", "苹果", "橘子", "香蕉", "苹果"]
# 在下面写你的代码（提示：先用 for 遍历，再判断水果名是否已在字典里）：
fru_list = {}
for i in fruits:
    if i in fru_list:
        fru_list[i] += 1
    else:
        fru_list[i] = 1
print(fru_list)

l = {}
for a in fruits:
    l[a] = l.get(a,0) + 1
print(l)

# 挑战题（选做，经典 FizzBuzz）：
# 循环打印 1 到 15：
#   能被 3 整除打印 "Fizz"，能被 5 整除打印 "Buzz"，
#   同时被 3 和 5 整除打印 "FizzBuzz"，其他数字直接打印数字本身
# 在下面写你的代码：
for b in range(1,16):
    if b % 3 == 0 and b % 5 == 0:
        print("FizzBuzz")
    elif b % 3 == 0: 
        print("Fizz")
    elif b % 5 == 0: 
        print("Buzz")
    else:
        print(b)


# ============================================================
# 自测区：第三部分写完后，把下面的注释逐个取消，运行本文件
# 如果没有任何报错输出，说明你的代码通过了测试
# ============================================================
# assert sum(range(1, 101)) == 5050          # 这行只是告诉你正确答案是 5050
# assert check(4) == "偶数"
# assert check(7) == "奇数"
# assert max(numbers) == 20                   # 这行验证第 17 题答案确实是 20
