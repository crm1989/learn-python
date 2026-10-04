# -*- coding: utf-8 -*-
# ============================================================
# 第 7 课 · 综合项目实战：智能记账本
# ------------------------------------------------------------
# 这是基础阶段的毕业设计：7 个功能，全部用前 6 课的知识。
#
# 你要填 6 个空（Ledger 类里的方法），从易到难：
#   1. add_bill        —— 第1课对象创建 + 第3课存盘
#   2. show_all        —— 第1课循环 + 第5课 __str__
#   3. monthly_summary —— 第6课 datetime 判断本月 + 第2课推导式
#   4. category_stats  —— 第1课字典统计
#   5. check_budget    —— 第1课 if 判断
#   6. export_report   —— 第3课文件写入 + f-string 排版
#
# 老规矩：休眠 CUE、每填完一个就 Ctrl+S 运行测试。
# 卡住超过 5 分钟说"提示第 X 个功能"。
# ============================================================

import json
import os
import datetime
from turtle import end_fill

DATA_FILE = "ledger.json"
BUDGET = 3000   # 每月支出预算（元），你可以改


# ------------------------------------------------------------
# Bill 类：一笔账（已写好，读懂即可）
# ------------------------------------------------------------
class Bill:
    """一笔账单：时间、类型(收入/支出)、类别、金额、备注"""

    def __init__(self, bill_type, category, amount, note=""):
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.bill_type = bill_type      # "收入" 或 "支出"
        self.category = category        # 如 "餐饮"、"交通"、"工资"
        self.amount = amount            # 金额（正数）
        self.note = note                # 备注，可为空字符串

    def __str__(self):
        return f"{self.time} | {self.bill_type} | {self.category} | {self.amount}元 | {self.note}"

    # ---- json 存取（第3课+第6课知识，已写好）----
    def to_dict(self):
        return {
            "time": self.time,
            "bill_type": self.bill_type,
            "category": self.category,
            "amount": self.amount,
            "note": self.note
        }

    @classmethod
    def from_dict(cls, d):
        """从字典还原 Bill 对象"""
        bill = cls.__new__(cls)   # 绕过 __init__，直接创建空对象
        bill.time = d["time"]
        bill.bill_type = d["bill_type"]
        bill.category = d["category"]
        bill.amount = d["amount"]
        bill.note = d["note"]
        return bill


# ------------------------------------------------------------
# Ledger 类：整个账本（6 个方法等你填）
# ------------------------------------------------------------
class Ledger:

    def __init__(self):
        self.bills = []      # Bill 对象的列表
        self.load()

    # ===== 空 1：记一笔 =====
    # 要求：
    #   ① 用参数创建 Bill 对象
    #   ② 加入 self.bills 列表
    #   ③ 调用 self.save() 立即存盘
    #   ④ 打印"已记录"
    def add_bill(self, bill_type, category, amount, note=""):
        bill = Bill(bill_type, category, amount, note)
        self.bills.append(bill)
        self.save()
        print("已记录")

    # ===== 空 2：查看明细 =====
    # 要求：
    #   ① 如果 self.bills 为空，打印"暂无记录"并 return
    #   ② 否则遍历打印每笔（直接 print(bill) 即可，__str__ 会生效）
    #   ③ 最后打印"共 X 笔"
    def show_all(self):
        if  not self.bills :
            print("暂无记录")
            return
        for bill in self.bills:
            print(bill)
        print(f"共{len(self.bills)}笔")

    # ===== 空 3：本月汇总 =====
    # 要求：
    #   ① 从 self.bills 中筛选出"本月"的记录
    #      提示：bill.time[:7] == 当前年月字符串
    #            当前年月 = datetime.datetime.now().strftime("%Y-%m")
    #   ② 分别计算本月收入总额、支出总额
    #      提示：推导式 sum(b.amount for b in 本月记录 if b.bill_type == "收入")
    #   ③ 打印：收入、支出、结余（收入-支出）
    def monthly_summary(self):
        s_sum = sum(b.amount for b in self.bills if b.time[:7] == datetime.datetime.now().strftime("%Y-%m") and b.bill_type == "收入")
        r_sum = sum(b.amount for b in self.bills if b.time[:7] == datetime.datetime.now().strftime("%Y-%m") and b.bill_type == "支出")
        print(f"收入:{s_sum}、支出:{r_sum}、结余（收入-支出）:{s_sum-r_sum}")

    # ===== 空 4：类别统计 =====
    # 要求：
    #   ① 只统计"支出"记录
    #   ② 按类别分组求和（提示：字典，键=类别，值=累计金额）
    #   ③ 打印每个类别及其总额
    def category_stats(self):
        sumlist = {}
        for b in self.bills:
            if b.time[:7] == datetime.datetime.now().strftime("%Y-%m") and b.bill_type == "支出":
                if b.category in sumlist:
                    sumlist[b.category] += b.amount
                else:
                    sumlist[b.category] = b.amount
        # print(sumlist)
        # for cat,amt in sumlist:
        for cat,amt in sumlist.items():
            print(f"类别{cat}的金额是{amt}")

    # ===== 空 5：预算提醒 =====
    # 要求：
    #   ① 计算本月支出总额（可以复用 monthly_summary 里的逻辑）
    #   ② 如果超过 BUDGET，打印警告：
    #      "警告！本月已支出 X 元，超出预算 Y 元！"
    #   ③ 否则打印："本月支出 X 元，预算剩余 Y 元"
    def check_budget(self):
        r_sum = sum(b.amount for b in self.bills if b.time[:7] == datetime.datetime.now().strftime("%Y-%m") and b.bill_type == "支出")
        if r_sum >= int(BUDGET):
            print(f"警告！本月已支出{r_sum}元，超出预算{r_sum-int(BUDGET)}元！")
        else:
            print(f"本月支出{r_sum}元，预算剩余{int(BUDGET)-r_sum}元！")

    # ===== 空 6：导出报表 =====
    # 要求：
    #   ① 生成文件名："report_2026-10.txt"（年月用 strftime）
    #   ② 用 "w" 模式写入，内容包括：
    #      - 标题行："===== 2026年10月 财务报表 ====="
    #      - 本月每笔明细（用 __str__ 格式）
    #      - 汇总行：收入、支出、结余
    #      - 类别统计
    #   ③ 打印"报表已导出：report_2026-10.txt"
    #   提示：可以调用 monthly_summary 和 category_stats 里的逻辑，
    #         但要把 print 改成 f.write
    def export_report(self):
        file_name = f"report_{datetime.datetime.now().strftime("%Y-%m")}.txt"
        file_name_j = f"report_{datetime.datetime.now().strftime("%Y-%m")}.json"
        title_name = f"===== {datetime.datetime.now().strftime("%Y")}年{datetime.datetime.now().strftime("%m")}月 财务报表 ====="
        if  not self.bills :
            print("暂无记录")
            return
        else:
            #json格式输出
            fileout = []
            with open(file_name_j,"w",encoding="utf-8") as f:
                fileout.append(title_name)
                for bill in self.bills:
                    fileout.append(bill.to_dict())
                s_sum = sum(b.amount for b in self.bills if b.time[:7] == datetime.datetime.now().strftime("%Y-%m") and b.bill_type == "收入")
                r_sum = sum(b.amount for b in self.bills if b.time[:7] == datetime.datetime.now().strftime("%Y-%m") and b.bill_type == "支出")
                fileout.append(f"收入:{s_sum}、支出:{r_sum}、结余（收入-支出）:{s_sum-r_sum}")
                json.dump(fileout,f,ensure_ascii=False)
            #文本格式输出
            with open(file_name,"w",encoding="utf-8") as f:
                f.write(title_name)
                for bill in self.bills:
                    f.write(f"\n{str(bill)}")
                f.write((f"\n收入:{s_sum}、支出:{r_sum}、结余（收入-支出）:{s_sum-r_sum}"))
            print ( f"报表已导出： {file_name} " )

    # ------------------------------------------------------------
    # 存取数据（已写好，第3课+第6课知识）
    # ------------------------------------------------------------
    def save(self):
        data = [b.to_dict() for b in self.bills]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.bills = [Bill.from_dict(d) for d in data]
            print(f"已加载 {len(self.bills)} 条记录")
        else:
            self.bills = []


# ------------------------------------------------------------
# 主菜单（已写好，不要改）
# ------------------------------------------------------------
def main():
    ledger = Ledger()
    print("智能记账本 v1.0")

    while True:
        print("\n1.记一笔  2.查看明细  3.本月汇总  4.类别统计  5.预算提醒  6.导出报表  7.退出")
        choice = input("选择：")

        if choice == "1":
            bill_type = input("类型（收入/支出）：").strip()
            if bill_type not in ("收入", "支出"):
                print("类型必须是 收入 或 支出")
                continue
            category = input("类别（餐饮/交通/工资等）：").strip()
            if not category:
                print("类别不能为空")
                continue
            amount_text = input("金额：").strip()
            try:
                amount = int(amount_text)
                if amount <= 0:
                    print("金额必须是正数")
                    continue
            except ValueError:
                print("金额必须是整数")
                continue
            note = input("备注（可空）：").strip()
            ledger.add_bill(bill_type, category, amount, note)

        elif choice == "2":
            ledger.show_all()

        elif choice == "3":
            ledger.monthly_summary()

        elif choice == "4":
            ledger.category_stats()

        elif choice == "5":
            ledger.check_budget()

        elif choice == "6":
            ledger.export_report()

        elif choice == "7":
            print("再见！")
            break

        else:
            print("无效选项")


if __name__ == "__main__":
    main()
