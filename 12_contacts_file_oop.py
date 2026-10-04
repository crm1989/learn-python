# -*- coding: utf-8 -*-
# ============================================================
# 毕业项目：面向对象版 · 文件通讯录
# ------------------------------------------------------------
# 和第 1 课通讯录（03_contacts_project.py）的区别：
#   第1课：数据是裸字典，程序一关数据就没了
#   本次：① 每个联系人是一个 Contact 对象（第5课）
#         ② AddressBook 类统管增删查+存盘读盘（第5课管理器类）
#         ③ 数据存在 contacts_data.txt，关掉重开联系人还在（第3课）
#
# 你要填 6 个 pass（从易到难）：
#   1. Contact.__str__              —— 热身
#   2. AddressBook.find             —— 字典 .get
#   3. AddressBook.remove           —— 先判断再删，返回 True/False
#   4. AddressBook.show_all         —— 编号遍历（enumerate 或计数器）
#   5. AddressBook.save             —— 对象写进文件
#   6. AddressBook.load             —— 从文件还原对象
#
# 菜单部分已经帮你写好，不要改。做完休眠 CUE 再动手。
# 运行：py 12_contacts_file_oop.py
# ============================================================

import os

DATA_FILE = "contacts_data.txt"   # 数据文件名（常量，全大写）


# ------------------------------------------------------------
# 第一部分：Contact 类 —— 一个联系人就是一个对象
# ------------------------------------------------------------
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # 【填空 1】__str__：返回 "姓名：电话" 格式的字符串
    # 提示：return f"{self.name}：{self.phone}"
    def __str__(self):
        return f"{self.name}：{self.phone}"

    # 把对象变成一行文本（存盘用）。这个方法已写好，读一遍理解即可
    def to_line(self):
        return f"{self.name},{self.phone}"

    # 把一行文本还原成对象（读盘用）。也已写好，注意复习 @classmethod
    @classmethod
    def from_line(cls, line):
        name, phone = line.strip().split(",")
        return cls(name, phone)


# ------------------------------------------------------------
# 第二部分：AddressBook 类 —— 通讯录管理器（核心）
# 内部用一个字典装联系人：self.contacts = {姓名: Contact对象}
# ------------------------------------------------------------
class AddressBook:
    def __init__(self):
        self.contacts = {}          # 键是姓名，值是 Contact 对象

    # 添加/更新（已写好）：同名联系人再次添加 = 更新电话
    def add(self, name, phone):
        self.contacts[name] = Contact(name, phone)

    # 【填空 2】find：按姓名查 Contact 对象
    #   找到 → 返回该 Contact 对象；找不到 → 返回 None
    #   提示：字典的 .get(键) 正好满足"找不到返回 None"
    def find(self, name):
        return self.contacts.get(name)

    # 【填空 3】remove：删除联系人
    #   先判断 name 在不在 self.contacts 里：
    #     在 → del 删除，return True
    #     不在 → return False
    def remove(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        else:
            return False

    # 【填空 4】show_all：编号打印所有联系人
    #   空的 → print("通讯录是空的")
    #   否则 → 从 1 开始编号，每行打印 "1. 小明：138" 这样
    #   提示：self.contacts.values() 能拿到所有 Contact 对象；
    #         每个对象直接 print 就会调用它的 __str__
    def show_all(self):
        if not self.contacts:
            print("通讯录是空的")
        else:
            for n, c in enumerate(self.contacts.values(), start=1):
                print(f"{n}. {c}")

    # 【填空 5】save：把所有联系人写入 DATA_FILE（覆盖写 "w"）
    #   每个 Contact 调 to_line() 变成 "小明,138"，再补 "\n" 写入
    #   提示：
    #     with open(DATA_FILE, "w", encoding="utf-8") as f:
    #         for c in self.contacts.values():
    #             f.write(c.to_line() + "\n")
    def save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for c in self.contacts.values():
                f.write(c.to_line() + "\n")

    # 【填空 6】load：程序启动时从文件读回联系人
    #   ① 先用 os.path.exists(DATA_FILE) 看文件在不在，不在就直接 return
    #   ② 以 "r" 打开，逐行读取
    #   ③ 每行用 Contact.from_line(line) 还原成对象
    #   ④ 存进字典：self.contacts[对象.name] = 对象
    def load(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                contact = Contact.from_line(line)
                self.contacts[contact.name] = contact

# ------------------------------------------------------------
# 第三部分：菜单主程序（已写好，不要改）
# 看懂它是怎么"组合"上面两个类的即可
# ------------------------------------------------------------
def main():
    book = AddressBook()
    book.load()                         # 一启动就从文件读回上次的数据
    print("已加载联系人", len(book.contacts), "人")

    while True:
        print()
        print("===== 文件通讯录 =====")
        print("1. 添加/更新联系人")
        print("2. 查询联系人")
        print("3. 删除联系人")
        print("4. 显示全部")
        print("5. 退出")
        choice = input("请选择（1-5）：")

        if choice == "1":
            name = input("姓名：").strip()
            phone = input("电话：").strip()
            if name:
                book.add(name, phone)
                book.save()             # 每次改动后立刻存盘
                print("已保存")
            else:
                print("姓名不能为空")

        elif choice == "2":
            name = input("要查询的姓名：").strip()
            contact = book.find(name)
            if contact:
                print("查到：", contact)
            else:
                print("查无此人")

        elif choice == "3":
            name = input("要删除的姓名：").strip()
            if book.remove(name):
                book.save()             # 删除后也要立刻存盘
                print("已删除")
            else:
                print("查无此人，无法删除")

        elif choice == "4":
            book.show_all()

        elif choice == "5":
            print("再见！")
            break

        else:
            print("无效选项，请重新输入")


if __name__ == "__main__":
    main()
