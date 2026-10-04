# -*- coding: utf-8 -*-
# ============================================================
# Python 第 5 课 · 综合测试卷
# 考察重点：class / __init__ / self / 方法 / 对象独立性 /
#           __str__ / 类变量与实例变量 / 管理器类 / 对象↔文本
# 复习抽查：键名拼写、选对数据源、文件 strip、精准异常类型
#
# 考试规则：
#   第一部分：先不要运行！读代码写下预测结果，全部写完再运行
#             （运行： py 11_lesson5_exercises.py）
#   第二部分：找错误，先说"错在哪、怎么改"，再动手
#   第三部分：动手写。做题前休眠 CUE（右下角 CUE 图标 → 休眠）
# ============================================================


print("【第一部分】看代码，写结果")
print("-" * 40)

# 第 1 题：两次调用分别打印什么？（self 的作用）
class Counter:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1

c1 = Counter()
c1.click()
c1.click()
c2 = Counter()
c2.click()
print("第1题：", c1.count, c2.count)

# 第 2 题：打印什么？
class Bottle:
    def __init__(self, water=0):
        self.water = water

    def drink(self, amount):
        self.water -= amount

b = Bottle(10)
b.drink(3)
print("第2题：", b.water)

# 第 3 题：print 这个对象显示什么？（__str__）
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}卖{self.price}元"

print("第3题：", Item("铅笔", 2))

# 第 4 题：方法返回什么？连续调用后结果？
class ScoreKeeper:
    def __init__(self):
        self.scores = []

    def add(self, s):
        self.scores.append(s)

    def avg(self):
        return sum(self.scores) / len(self.scores)

k = ScoreKeeper()
k.add(80)
k.add(100)
print("第4题：", k.avg())

# 第 5 题：三个结果分别是什么？（类变量共享 vs 实例变量独有）
class Cat:
    species = "猫科"
    def __init__(self, name):
        self.name = name

a = Cat("咪咪")
b = Cat("橘座")
print("第5题：", a.species, a.name, b.name)

# 第 6 题：管理器类——查找结果分别是什么？
class Box:
    def __init__(self):
        self.items = {}
    def put(self, key, value):
        self.items[key] = value
    def get(self, key):
        return self.items.get(key)

box = Box()
box.put("橡皮", "文具")
print("第6题：", box.get("橡皮"), box.get("尺子"))

# 第 7 题（第 4 课复习）：lambda 排序后姓名顺序？
products = [
    {"name": "A书", "stock": 5},
    {"name": "B笔", "stock": 20},
    {"name": "C本", "stock": 12},
]
ps = sorted(products, key=lambda p: p["stock"], reverse=True)
print("第7题：", [p["name"] for p in ps])


print()
print("【第二部分】找出错误")
print("-" * 40)
print("以下 4 段代码都有问题。先说出错因和改法，再动手改。")

# 第 8 题（调用时报错：方法定义漏了 self）：
#
class Lamp:
    def __init__(self):
        self.on = False
    def toggle(self):
        self.on = not self.on

lamp = Lamp()
lamp.toggle()

# 第 9 题（不报错，但作者的意图没实现——改了一个，另一个也变了？
#        想想第 4 课的“共享可变对象”）：
#
class Team:
    def __init__(self):
        self.members = []
    def add(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()
t1.add("甲")
print(t2.members)      # 作者希望是空的，结果呢？应该怎么改？

# 第 10 题（对象取值写错符号，第 4 课错题复习）：
#
# class Student:
#     def __init__(self, name):
#         self.name = name
# s = Student("小明")
# print(s.name)          # 这行没问题
# print(s("name"))       # 这行为什么报错？应该怎么写？

# 第 11 题（第 3 课复习 · 异常类型不精准）：
#
# try:
#     num = int(input("输入数字："))
# except ValueError:                # ← 这样写有什么问题？应该写什么？
#     print("出错了")

print()
print("【第三部分】动手写代码")
print("-" * 40)

# 第 12 题（定义你的第一个完整类）：写一个 Rectangle 矩形类
# 要求：
#   __init__(self, width, height)：保存宽和高
#   area(self)：返回面积（宽 × 高）
#   __str__(self)：返回 "宽x高 的矩形，面积=X" 这样的字符串
# 然后创建 r = Rectangle(3, 4)，打印 r.area() 和 r
class Rectangle:
    # pass  # 在下面写代码（删掉 pass）
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"宽{self.width}x高{self.height}的矩形，面积={self.area()}"

r = Rectangle(3, 4)
print(r.area())
print(r)

# 第 13 题（对象独立性 + 拼写检查）：写一个 ShoppingCart 购物车类
# 要求：
#   __init__ 里初始化 self.goods = []（注意键/属性名拼写，下面都用同一个名字）
#   add(self, name)：把商品名追加进 self.goods
#   total(self)：返回商品件数
# 创建两个购物车 cart_a、cart_b，各自添加商品，验证互不影响
class ShoppingCart:
    def __init__(self):
        self.goods = []
    def add(self,name):
        self.goods.append(name)
    def total(self):
        return len(self.goods)

cart_a = ShoppingCart()
cart_b = ShoppingCart()
cart_a.add("apple")
cart_a.add("banana")
cart_b.add("orange")

# 第 14 题（管理器类 + 第1课“先判断再删”）：完善下面的 Notebook 类
# add 已写好。请你补两个方法：
#   find(self, title)：有则返回内容，没有返回 None（用字典 .get）
#   delete(self, title)：先判断在不在，在就删除并返回 True，不在返回 False
class Notebook:
    def __init__(self):
        self.notes = {}

    def add(self, title, content):
        self.notes[title] = content

    # 在下面写 find：
    def find(self, title):
        return self.notes.get(title)
    # 在下面写 delete：
    def delete(self,title):
        if title in self.notes:
            del self.notes[title]
            return True
        else:
            return False

book = Notebook()
book.add("购物", "牛奶、鸡蛋")
# 写两行测试：打印 find("购物")、delete("不存在的标题") 的结果
print(book.find("购物"))
print(book.find("购物1"))
print(book.delete("购物"))
print(book.delete("购物"))

# 第 15 题（对象 ↔ 文本，毕业项目预热）：完善 Member 类
#   to_line(self)：返回 "姓名,年龄" 格式的字符串（存盘用，不要求带\n）
#   from_line(cls, line)：@classmethod，把 "小明,12" 这种行还原成 Member 对象
#                         （记得先 strip，再 split，年龄要 int 转换）
class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __dir__(self):
        pass
    # 在下面写 to_line：
    def to_line(self):
        return f"{self.name},{self.age}"
    # 在下面写 from_line：
    @classmethod
    def from_line(cls,line):
        name,age = line.strip().split(",")
        return cls(name,int(age))

print(Member.from_line("小红,11").age)

# 挑战题（文件 + 类的综合）：
# 用第 15 题的 Member 类：
# 1) 把两个成员 [Member("小明", 12), Member("小红", 11)] 写入 members.txt，每行一个
#    （提示：for 循环里调用 m.to_line()，再补上 "\n" 写入）
# 2) 再从文件读回，每行用 Member.from_line 还原成对象，
#    收集到列表 loaded_members
# 3) 打印 loaded_members 中每个人的 name 和 age（验证对象真的还原成功）
# 在下面写代码：
mb = [Member("小明", 12).to_line(),Member("小红", 11).to_line()]
with open("members.txt","w",encoding="UTF-8") as wr:
    for m in mb:
        wr.write(f"{m}\n")

loaded_members = []
with open("members.txt","r",encoding="UTF-8") as lines:
    for line in lines:
        loaded_members.append(Member.from_line(line))

for m in loaded_members: 
    print (m.name, m.age)

# ============================================================
# 自测区：写完后取消注释运行，没有任何输出 = 全部通过
# ============================================================
# assert r.area() == 12
# assert str(r) == "3x4 的矩形，面积=12"
# assert cart_a.total() != cart_b.total() or True
# assert book.find("购物") == "牛奶、鸡蛋"
# assert book.delete("不存在的标题") == False
# assert Member("小明", 12).to_line() == "小明,12"
# assert Member.from_line("小红,11").age == 11
# assert loaded_members[0].name == "小明" and loaded_members[1].age == 11
