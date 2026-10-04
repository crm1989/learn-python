# -*- coding: utf-8 -*-
# ============================================================
# Python 第 4 课：函数进阶 + 模块
# 运行方法： py 08_lesson4_functions_advanced.py
# 学习方法： 对照运行结果阅读；本课偏“招式”，每个知识点都短小实用
# ============================================================


# ------------------------------------------------------------
# 知识点 1：默认参数 —— 调用时不传就用默认值
# ------------------------------------------------------------
print("=" * 50)
print("知识点 1：默认参数")
print("=" * 50)

def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

print(greet("小明"))            # 不传第二个参数 → 用默认值"你好"
print(greet("小明", "早上好"))  # 传了 → 覆盖默认值


# ------------------------------------------------------------
# 知识点 2：关键字参数 —— 调用时“指名道姓”，可读性更好
#   好处1：不用记参数顺序
#   好处2：看到调用代码就知道每个值是什么意思
# ------------------------------------------------------------
print("=" * 50)
print("知识点 2：关键字参数")
print("=" * 50)

def make_coffee(size, milk=False, sugar=0):
    desc = f"{size}杯咖啡"
    if milk:
        desc += " + 牛奶"
    if sugar:
        desc += f" + {sugar}份糖"
    return desc

print(make_coffee("大", sugar=2))          # 跳过 milk，直接指定 sugar
print(make_coffee(size="中", milk=True))   # 全部指名道姓


# ------------------------------------------------------------
# 知识点 3：经典陷阱 —— 默认参数不能用可变对象！
#   默认值只在函数定义时创建一次，
#   用列表/字典当默认值时，所有调用会共享同一个对象
# ------------------------------------------------------------
print("=" * 50)
print("知识点 3：可变默认参数的坑（面试高频题）")
print("=" * 50)

def add_item_bad(item, basket=[]):   # 错误示范！
    basket.append(item)
    return basket

print(add_item_bad("苹果"))   # ['苹果']  正常
print(add_item_bad("香蕉"))   # ['苹果', '香蕉']  ← 惊不惊喜？上次的苹果还在！

# 正确写法：默认值用 None，函数内部再创建新列表
def add_item_good(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item_good("苹果"))  # ['苹果']
print(add_item_good("香蕉"))  # ['香蕉']  这次干净了


# ------------------------------------------------------------
# 知识点 4：多个返回值 —— return 后面逗号隔开，接收时解包
# ------------------------------------------------------------
print("=" * 50)
print("知识点 4：多个返回值")
print("=" * 50)

def min_max(nums):
    return min(nums), max(nums)   # 一次返回两个值（其实是个元组）

lo, hi = min_max([3, 1, 4, 1, 5])  # 用两个变量分别接收
print("最小值：", lo, "最大值：", hi)


# ------------------------------------------------------------
# 知识点 5：*args 不定长参数 —— 想传几个就传几个
#   函数内部 args 是一个元组
# ------------------------------------------------------------
print("=" * 50)
print("知识点 5：*args 不定长参数")
print("=" * 50)

def total(*args):
    s = 0
    for n in args:
        s += n
    return s

print(total(1, 2, 3))         # 3 个参数
print(total(1, 2, 3, 4, 5))   # 5 个参数也行
print(total())                # 0 个参数也不报错


# ------------------------------------------------------------
# 知识点 6：作用域 —— 函数内外的变量是两回事
#   函数内部赋值的变量 = 局部变量，函数外看不到
#   函数只是“读取”外部变量没问题，但“赋值”会创建自己的局部变量
# ------------------------------------------------------------
print("=" * 50)
print("知识点 6：作用域（局部 vs 全局）")
print("=" * 50)

x = 10                        # 全局变量

def try_change():
    x = 99                    # 这行创建了一个“局部变量 x”，跟全局的 x 无关！
    print("函数内看到的 x =", x)

try_change()
print("函数外看到的 x =", x)  # 还是 10，没被改变


def really_change():
    global x                  # 声明“我要改的是全局的 x”（能用但别常用）
    x = 99

really_change()
print("用 global 后的 x =", x)


# ------------------------------------------------------------
# 知识点 7：lambda —— 一次性小函数
#   lambda 参数: 表达式   （冒号前是参数，冒号后是返回值）
#   单独定义用得少，真正的用武之地是给 sorted() 指定排序规则
# ------------------------------------------------------------
print("=" * 50)
print("知识点 7：lambda 与排序实战")
print("=" * 50)

# 等价关系演示
def square(n):
    return n ** 2
square_lambda = lambda n: n ** 2
print(square(5), square_lambda(5))   # 两个结果一样

# 实战：按分数给学生排序（key 指定“按什么排”）
students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 72},
]
ranked = sorted(students, key=lambda s: s["score"], reverse=True)
for i, s in enumerate(ranked, start=1):    # enumerate 带起始编号（第2课）
    print(f"第{i}名 {s['name']} {s['score']}分")

# 字符串排序也能用 key：忽略大小写
words = ["banana", "Apple", "cherry"]
print(sorted(words))                       # 大写反而排前面（按字符编码）
print(sorted(words, key=str.lower))        # 按小写比较，符合直觉


# ------------------------------------------------------------
# 知识点 8：模块 —— 站在标准库和自己的代码肩膀上
#   import 模块名            → 用 模块名.功能()
#   from 模块 import 功能    → 直接用 功能()
#   你写的每个 .py 文件都是一个模块！
# ------------------------------------------------------------
print("=" * 50)
print("知识点 8：模块导入")
print("=" * 50)

import math
print("math.sqrt(16) =", math.sqrt(16))    # 平方根
print("math.pi =", math.pi)                # 圆周率

from random import randint
print("掷骰子：", randint(1, 6))           # 1~6 的随机整数

import datetime
print("现在是：", datetime.datetime.now())

# 导入自己写的模块（同文件夹下的 my_utils.py）
import my_utils
print(my_utils.shout("hello"))             # 用 模块名.函数名()
print(my_utils.add(1, 2))


# ------------------------------------------------------------
# 知识点 9：if __name__ == "__main__" —— 文件的“双面人生”
#   每个文件都有个内置变量 __name__：
#   - 直接运行这个文件时，__name__ == "__main__"
#   - 被别人 import 时，__name__ == "文件名"
#   所以 my_utils.py 里被保护的代码：
#   - 你直接 py my_utils.py → 会执行（当自测）
#   - 刚才 import my_utils   → 不执行（不会刷屏）
# ------------------------------------------------------------
print("=" * 50)
print("知识点 9：if __name__ == \"__main__\"")
print("=" * 50)
print("刚才 import my_utils 时，你有没有看到它的自测输出？——没有！")
print("因为那些代码被 if __name__ == \"__main__\" 保护着")
print("现在去终端运行： py my_utils.py  —— 就能看到自测输出了")
print("这就是“一个文件既能当工具被导入，又能自己运行测试”的秘密")


# ============================================================
# 本课小结（必须带走的 5 个能力）：
# 1. 默认参数让函数更灵活；关键字参数让调用更易读
# 2. 可变默认参数([]/{})是大坑，正确写法是默认 None 函数内创建
# 3. return a, b 返回多个值，接收时 lo, hi = f()
# 4. lambda 参数: 表达式，最常用在 sorted(key=lambda ...) 排序
# 5. import 三种姿势 + if __name__ == "__main__" 保护自测代码
#    下次看到别人的代码结尾有这一句，你就知道为什么了
# ============================================================
