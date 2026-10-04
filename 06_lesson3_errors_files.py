# -*- coding: utf-8 -*-
# ============================================================
# Python 第三课：异常处理（try/except）+ 文件读写
# 运行方法： py 06_lesson3_errors_files.py
# 学习方法： 对照运行结果阅读，重点理解“报错不崩溃”和“数据存硬盘”
# ============================================================


# ------------------------------------------------------------
# 知识点 1：没有保护时，程序遇到错误会“当场死亡”
# ------------------------------------------------------------
print("=" * 50)
print("知识点 1：程序为什么需要 try")
print("=" * 50)
print("下面演示一个会报错的转换（已用 try 保护，程序不会死）：")

# int() 只能转换长得像数字的字符串，转换字母会抛 ValueError
try:
    age = int("abc")          # 这行会抛出 ValueError
    print("转换成功：", age)  # 出错后这行不会执行
except ValueError:
    print("转换失败：'abc' 不是合法数字")

print("你看，程序还活着，继续往下执行了！")
print("如果没有 try/except，程序会在 int('abc') 那行直接崩溃退出")


# ------------------------------------------------------------
# 知识点 2：try / except 的完整结构
#   try    : 放“可能出错”的代码
#   except : 出错后执行的补救代码（可以写多个，分别处理不同错误）
#   else   : 没出错才执行
#   finally: 无论出不出错都执行（了解即可）
# ------------------------------------------------------------
print("=" * 50)
print("知识点 2：try / except / else / finally")
print("=" * 50)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:        # 专门处理“除以 0”
        return "除数不能是 0"
    else:
        print("计算顺利完成", end="，")
        return result
    finally:
        print("（本次计算结束）")      # 无论成败都会打印

print(safe_divide(10, 2))
print(safe_divide(10, 0))


# ------------------------------------------------------------
# 知识点 3：新手最常见的 4 种错误（认识名字，才能精准接住）
# ------------------------------------------------------------
print("=" * 50)
print("知识点 3：常见异常类型")
print("=" * 50)

# ValueError：值不对（类型对，但内容无法转换）
try:
    int("12.5")
except ValueError:
    print("ValueError：值的内容不合法（'12.5' 不能直接转 int）")

# KeyError：字典里没有这个键
try:
    d = {"name": "小明"}
    print(d["age"])
except KeyError:
    print("KeyError：字典里没有 'age' 这个键")

# IndexError：列表下标越界（还记得第 13 题吗？）
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("IndexError：下标 10 超出了列表范围")

# FileNotFoundError：文件不存在（下一部分马上用到）
try:
    open("一个不存在的文件.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("FileNotFoundError：要打开的文件不存在")

print()
print("口诀：except 后面写的错误类型越精准越好")
print("不要偷懒写空 except —— 那样会把你自己的 bug 也藏起来")


# ------------------------------------------------------------
# 知识点 4：实战 —— 让 input 程序“输不错”
# 这是菜单程序的必备技能：用户输入字母也不崩溃，而是重新输入
# ------------------------------------------------------------
print("=" * 50)
print("知识点 4：输入校验的标准套路（while + try）")
print("=" * 50)

def input_age(prompt):
    while True:                          # 不停循环，直到输入合法
        text = input(prompt)
        try:
            value = int(text)            # 试着转数字
            if value < 0:
                print("年龄不能是负数，请重输")
                continue                 # 跳过本轮，继续循环
            return value                 # 转换成功，跳出函数
        except ValueError:
            print("这不是整数，请重新输入")

# 本文件演示时不等待键盘输入，下面这行先注释；你可以取消注释亲手试试：
# my_age = input_age("请输入你的年龄：")
# print("你的年龄是：", my_age)
print("（input_age 函数已定义，取消上面注释可亲自体验输错不崩溃）")


# ------------------------------------------------------------
# 知识点 5：写文件 —— 把数据永久存到硬盘
#   open(文件路径, 模式, encoding="utf-8")
#   模式 "w" = write 写入（会清空旧内容！）
#        "a" = append 追加（在文件末尾加内容）
#   with open(...) as f: 用完自动关闭文件，是标准写法
# ------------------------------------------------------------
print("=" * 50)
print("知识点 5：写文件")
print("=" * 50)

with open("demo_file.txt", "w", encoding="utf-8") as f:
    f.write("第一行内容\n")              # \n 是换行符
    f.write("第二行内容\n")
    f.write("小明,13800000000\n")        # 用逗号分隔多个字段（简易表格）
print("已经把 3 行内容写入 demo_file.txt")
print("去项目文件夹里能找到这个文件，用记事本可以打开看")

# 追加模式：不清空，在后面继续加
with open("demo_file.txt", "a", encoding="utf-8") as f:
    f.write("小红,13900000000\n")
print("又追加了 1 行")


# ------------------------------------------------------------
# 知识点 6：读文件 —— 把硬盘上的数据读回程序
#   模式 "r" = read 读取
# ------------------------------------------------------------
print("=" * 50)
print("知识点 6：读文件")
print("=" * 50)

# 读法 1：read() 一次性读成一个大字符串
with open("demo_file.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("read() 读到的全部内容：")
print(content)

# 读法 2：一行一行读（文件大时推荐，配合 for）
print("逐行读取并处理：")
with open("demo_file.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()             # 去掉行尾的 \n 和空白（第2课的 strip！）
        print("拿到一行：", line)


# ------------------------------------------------------------
# 知识点 7：综合实战 —— 用文本文件保存“表格数据”
# 约定：每行一条记录，字段之间用逗号分隔
# 写入用 join，读取用 split —— 正好用上第二课的内容！
# ------------------------------------------------------------
print("=" * 50)
print("知识点 7：保存结构化数据（通讯录雏形）")
print("=" * 50)

# 内存里的数据（列表装字典，第 2 课的嵌套结构）
people = [
    {"name": "小明", "phone": "138"},
    {"name": "小红", "phone": "139"},
]

# 保存：每个字典拼成 "姓名,电话" 一行
with open("demo_contacts.txt", "w", encoding="utf-8") as f:
    for p in people:
        line = p["name"] + "," + p["phone"] + "\n"
        f.write(line)
print("已保存到 demo_contacts.txt")

# 读取：每行 split(",") 切回两个字段，重新组装成字典
loaded = []
with open("demo_contacts.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":                  # 跳过空行，防止最后多一个换行时报错
            continue
        name, phone = line.split(",")   # 切出两段，分别赋值给两个变量
        loaded.append({"name": name, "phone": phone})
print("重新读回程序的数据：", loaded)
print("这就是程序关闭后数据不丢失的秘密！")


# ------------------------------------------------------------
# 知识点 8：判断文件是否存在（读取前的安全检查）
# ------------------------------------------------------------
print("=" * 50)
print("知识点 8：读文件前先判断存在性")
print("=" * 50)
import os   # os 是标准库，专门和操作系统打交道

filename = "maybe_not_exist.txt"
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print(f"文件 {filename} 不存在，跳过读取（程序没崩溃）")
print("os.path.exists() 返回 True/False，是文件程序的常用门卫")


# ============================================================
# 本课小结（必须带走的 5 个能力）：
# 1. try 放可能出错的代码，except 写精准的错误类型
# 2. 四大常见错误：ValueError / KeyError / IndexError / FileNotFoundError
# 3. while True + try/except 是“输入校验”的标准套路
# 4. with open(路径, 模式, encoding="utf-8") 是读写文件的标准写法
#    "w" 覆盖写、"a" 追加、"r" 读；\n 换行
# 5. 表格数据存文本：写入用 "字段1,字段2\n"，读取用 strip + split(",")
#
# 本课运行后会在文件夹里生成 demo_file.txt 和 demo_contacts.txt，
# 可以打开看看，它们就是下一个项目“文件版通讯录”的基础。
# ============================================================
