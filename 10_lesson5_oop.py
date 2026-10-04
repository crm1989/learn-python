# -*- coding: utf-8 -*-
# ============================================================
# Python 第 5 课：面向对象（类与对象）
# 运行方法： py 10_lesson5_oop.py
# 学习方法： 对照运行结果阅读。本课概念最抽象，记住一句话：
#           “类是图纸，对象是按图纸造出来的实物”
# ============================================================


# ------------------------------------------------------------
# 知识点 1：为什么需要类？—— 字典的烦恼
#   前面我们用字典表示学生：{"name": "小明", "scores": [90, 80]}
#   问题：数据（成绩）和操作数据的函数（算平均分）是分离的，
#   而且每个人都要记得字典里有哪些键、怎么算平均，容易写错。
#   类可以把“数据”和“操作数据的方法”打包在一起。
# ------------------------------------------------------------
print("=" * 50)
print("知识点 1：从字典到类")
print("=" * 50)

# 字典写法：数据是数据，函数是函数
stu_dict = {"name": "小明", "scores": [90, 80]}
def average(stu):
    return sum(stu["scores"]) / len(stu["scores"])
print("字典写法算平均：", average(stu_dict))


# ------------------------------------------------------------
# 知识点 2：定义类、创建对象、self 是什么
#   class 类名:           —— 画一张“图纸”
#   def __init__(self):   —— 构造方法：造对象时自动调用，用来装初始数据
#   self                  —— “我自己这个对象”，每个对象都有自己的一份数据
#   类名()                 —— 按图纸造出一个真实对象
# ------------------------------------------------------------
print("=" * 50)
print("知识点 2：class / __init__ / self")
print("=" * 50)

class Student:
    def __init__(self, name):
        self.name = name            # 给这个对象贴上 name 数据
        self.scores = []            # 每个学生都有自己的成绩列表

    # 下面知识点 3：方法 —— 打包在类里的函数，第一个参数永远是 self
    def add_score(self, score):
        self.scores.append(score)   # 操作“我自己”的成绩

    def average(self):
        return sum(self.scores) / len(self.scores)

print("=" * 50)
print("知识点 3：方法 —— 数据和操作长在同一个对象上")
print("=" * 50)
# 按图纸造两个对象（这正好是第 4 课 make_student 的升级版）
ming = Student("小明")
hong = Student("小红")
ming.add_score(90)
ming.add_score(80)
hong.add_score(70)
print("小明的平均：", ming.average())   # 数据和方法长在同一个对象上
print("小红的平均：", hong.average())
print("两人的成绩互不影响：", ming.scores, hong.scores)


# ------------------------------------------------------------
# 知识点 4：对象的独立性 —— self.scores 每次新建
#   __init__ 在每次 Student(...) 时执行一次，
#   里面的 self.scores = [] 每次都是新列表，绝不共享
#   （这就是第4课“可变默认参数坑”在类里的天然安全写法）
# ------------------------------------------------------------
print("=" * 50)
print("知识点 4：每个对象各有各的数据")
print("=" * 50)
a = Student("甲")
b = Student("乙")
a.add_score(100)
print("甲加了成绩，乙还是空的：", a.scores, b.scores)


# ------------------------------------------------------------
# 知识点 5：__str__ —— 让 print(对象) 显示得像个人话
#   不定义它，print 对象只会显示 <__main__.Student object at 0x...>
#   定义后，print 时自动调用，返回什么字符串就显示什么
# ------------------------------------------------------------
print("=" * 50)
print("知识点 5：__str__ 让对象更好看")
print("=" * 50)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"小狗（名字：{self.name}，{self.age}岁）"

d = Dog("旺财", 3)
print(d)                    # 自动调用 __str__
print(str(d))               # 效果一样


# ------------------------------------------------------------
# 知识点 6：对象也能做判断、做计算 —— 自定义方法
#   方法里可以写任意逻辑：if、循环、返回值，和普通函数一样
# ------------------------------------------------------------
print("=" * 50)
print("知识点 6：带业务逻辑的方法")
print("=" * 50)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):          # 存款
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):         # 取款：余额不足不能取
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

acc = Account("小明", 100)
acc.deposit(50)
print("存款后：", acc.balance)
print("取 200 成功吗：", acc.withdraw(200))   # False，余额只有150
print("取 30 成功吗：", acc.withdraw(30))     # True
print("最终余额：", acc.balance)


# ------------------------------------------------------------
# 知识点 7：类变量 vs 实例变量
#   写在 class 里、方法外面 = 类变量：所有对象共享一份
#   self.xxx = ...                  = 实例变量：每个对象各自一份
# ------------------------------------------------------------
print("=" * 50)
print("知识点 7：类变量（共享）与实例变量（独有）")
print("=" * 50)

class Car:
    wheels = 4                  # 类变量：所有汽车都有4个轮子（共享）

    def __init__(self, brand):
        self.brand = brand      # 实例变量：每辆车品牌不同（独有）

c1 = Car("比亚迪")
c2 = Car("特斯拉")
print("轮子数（共享）：", c1.wheels, c2.wheels, Car.wheels)
print("品牌（独有）：", c1.brand, c2.brand)


# ------------------------------------------------------------
# 知识点 8：管理器类 —— 一个对象管理一批对象
#   这是“面向对象版通讯录”的核心结构：
#   AddressBook 对象内部用字典装很多 Contact，
#   并提供 add / find / remove 等方法。数据怎么存被“藏”在类内部。
# ------------------------------------------------------------
print("=" * 50)
print("知识点 8：管理器类（通讯录雏形）")
print("=" * 50)

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"

class AddressBook:
    def __init__(self):
        self.contacts = {}               # 键=姓名，值=Contact对象

    def add(self, name, phone):
        self.contacts[name] = Contact(name, phone)

    def find(self, name):
        return self.contacts.get(name)   # 找不到返回 None，不报错

    def remove(self, name):
        if name in self.contacts:        # 先判断再删（第1课的好习惯）
            del self.contacts[name]
            return True
        return False

    def show_all(self):
        for c in self.contacts.values():
            print("  ", c)               # 自动用 Contact 的 __str__

book = AddressBook()
book.add("小明", "138")
book.add("小红", "139")
print("查到：", book.find("小明"))
print("查老王：", book.find("老王"))
book.show_all()


# ------------------------------------------------------------
# 知识点 9：对象 ↔ 字典/文本 —— 为“存文件”做准备
#   文件里只能存文字，不能直接存对象。
#   所以存盘前：对象 → 字典/一行文字（叫“序列化”）
#   读盘后：一行文字 → 字典 → 对象（叫“反序列化”）
#   下节课的项目就靠这两个方法实现“关掉程序数据不丢”。
# ------------------------------------------------------------
print("=" * 50)
print("知识点 9：对象与文本的互相转换")
print("=" * 50)

class Contact2:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_line(self):                       # 对象 → 文本行（存盘用）
        return f"{self.name},{self.phone}"

    @classmethod                             # 先记住这个写法，下节课细讲
    def from_line(cls, line):                # 文本行 → 对象（读盘用）
        name, phone = line.strip().split(",")
        return cls(name, phone)

c = Contact2("小明", "138")
line = c.to_line()
print("存进文件的一行文字：", repr(line))     # repr 能看见 \n 之类的隐藏字符
c2 = Contact2.from_line("小红,139")
print("从文字还原出的对象：", c2.name, c2.phone)
print("这就是文件版通讯录的最后一块拼图！")


# ============================================================
# 本课小结（必须带走的 5 个能力）：
# 1. 类是图纸：class 定义；对象 = 类名() 造出来
# 2. __init__ 装初始数据，self 代表“当前这个对象”
# 3. 方法第一个参数永远是 self；对象.方法() 调用
# 4. 实例变量各自一份；__str__ 决定 print 出来长什么样
# 5. 对象转文字(to_line)、文字转对象(from_line) 是文件存盘的桥梁
#
# 下节课项目：用 Contact + AddressBook 重写通讯录，
# 启动时从文件读、增删后自动存，关掉重开数据还在。
# ============================================================
