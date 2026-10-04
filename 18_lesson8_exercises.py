# -*- coding: utf-8 -*-
# ============================================================
# 第 8 课测试卷：第三方库 / HTTP / API / JSON
# ------------------------------------------------------------
# 规则：
#   1. 休眠 CUE 再开始
#   2. 每做完一题就 Ctrl+S
#   3. 第一部分先写预测，全写完再运行对照（部分题要联网）
#   4. 第三部分变量名必须严格按题目要求（自测区 assert 用）
# ============================================================

import json
from socket import timeout
from tkinter import N
import requests


def 标题(文字):
    print("\n==========", 文字, "==========")


# ============================================================
# 第一部分：看代码，写结果（1–7 题）
# 把预测写在每题的注释里，写完再运行对照
# ============================================================

# --- 第 1 题：GET + 三件套 -----------------------------------
标题("第 1 题：GET 三件套")
try:
    r = requests.get("https://jsonplaceholder.typicode.com/posts/3", timeout=10)
    data = r.json()
    print("状态码 =", r.status_code)
    print("data 类型 =", type(data).__name__)
    print("userId =", data["userId"], "| id =", data["id"])
except requests.RequestException:
    print("（网络不可用）")
# 你的预测：
#   状态码 = ___
#   data 类型 = ___
#   userId = ___，id = ___


# --- 第 2 题：params 的"数字变字符串"坑 ----------------------
标题("第 2 题：params 参数类型")
try:
    r = requests.get("https://httpbin.org/get",
                     params={"score": 100, "level": "A"}, timeout=10)
    args = r.json()["args"]
    print("score =", args["score"], "，类型是", type(args["score"]).__name__)
except requests.RequestException:
    print("（网络不可用）")
# 你的预测：score = ___，类型是 ___（int 还是 str？）


# --- 第 3 题：POST 的 json body 保类型 ------------------------
标题("第 3 题：POST 的 body")
try:
    r = requests.post("https://httpbin.org/post",
                      json={"qty": 3, "name": "笔记本"}, timeout=10)
    body = r.json()["json"]
    print("qty =", body["qty"], "，类型是", type(body["qty"]).__name__)
except requests.RequestException:
    print("（网络不可用）")
# 你的预测：qty = ___，类型是 ___（和第 2 题对比！）


# --- 第 4 题：状态码（复习） -----------------------------------
标题("第 4 题：状态码")
try:
    ok = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    bad = requests.get("https://jsonplaceholder.typicode.com/posts/999", timeout=10)
    print("存在 →", ok.status_code, "，不存在 →", bad.status_code)
except requests.RequestException:
    print("（网络不可用）")
# 你的预测：存在 → ___，不存在 → ___


# --- 第 5 题：json() 和 text 的区别 ---------------------------
标题("第 5 题：text vs json()")
try:
    r = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    print("text 类型 =", type(r.text).__name__)
    print("json() 类型 =", type(r.json()).__name__)
    print("json() 取字段 name =", r.json()["name"])
except requests.RequestException:
    print("（网络不可用）")
# 你的预测：text 类型 = ___，json() 类型 = ___，name = ___


# --- 第 6 题：第 6 课复习 · json.loads/dumps 方向 -------------
标题("第 6 题：第 6 课复习")
text = '{"city": "Tokyo", "temp": 25}'
obj = json.loads(text)
print(type(obj).__name__, obj["city"])
back = json.dumps(obj, ensure_ascii=False)
print(type(back).__name__, back)
# 你的预测：第一行 = ___ ___，第二行 = ___ ___


# --- 第 7 题：推导式从 API 数据里筛选 --------------------------
标题("第 7 题：推导式筛选")
users = [
    {"name": "小明", "age": 30},
    {"name": "小红", "age": 25},
    {"name": "小刚", "age": 35},
]
names = [u["name"] for u in users if u["age"] >= 30]
print(names)
# 你的预测：___


# ============================================================
# 第二部分：找错误（8–11 题）
# 每段代码都有一个错误。先口头说出错在哪、怎么改，再动手改。
# ============================================================

# --- 第 8 题：缺了 timeout + 异常处理 -------------------------
标题("第 8 题：网络请求裸奔")
# 这段代码在断网或超时时会怎样？应该补上哪两件保险？
# 修复这段（改成安全写法）：
try:
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout = 5)
    print(r.json()["title"])
except requests.RequestException:
    print("network error")

#
# 参考答案提示：timeout=10 + try/except requests.RequestException


# --- 第 9 题：GET 却用了 json= ---------------------------
标题("第 9 题：GET 用错参数名")
# 想用 GET 带参数查询，但写成了 POST 的参数名。
# 下面这行错在哪？改成什么？
#   r = requests.get("https://httpbin.org/get", json={"q": "python"})
# 修复：
r = requests.post("https://httpbin.org/get", json={"q": "python"})

# --- 第 10 题：响应没调用 json() 就当字典用 --------------------
标题("第 10 题：text 当字典用")
# 下面代码运行会报错，为什么？怎么改？
#   r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
#   print(r.text["title"])
# 修复：
r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
print(r.json()["title"])

# --- 第 11 题：第 6 课复习 · json.load 传错类型 -----------------
标题("第 11 题：json.load 传字符串")
# 下面代码报错，为什么？json.load 应该接收什么？
#   with open("data.json", "r", encoding="utf-8") as f:
#       obj = json.load(f.read())
# 修复：
with open("books.json", "r", encoding="utf-8") as f:
    obj = json.load(f)

# ============================================================
# 第三部分：动手写代码（12–15 题 + 挑战题）
# 变量名必须严格按题目要求，写完取消文件末尾 assert 验证
# ============================================================

# --- 第 12 题：GET 取一条数据并存字段 -------------------------
标题("第 12 题：GET 取数据")
# 要求：GET https://jsonplaceholder.typicode.com/users/1
#       把返回 JSON 里的 "username" 字段存入变量 username（字符串）
#       打印出来
# 提示：requests.get(...) → .json() → ["username"]
#
# username = None   # ← 删掉这行，自己写代码，结果存到 username
try:
    r = requests.get("https://jsonplaceholder.typicode.com/users/1",timeout=10)
    print(r.json()["username"])
except requests.RequestException:
    print("network error")

# --- 第 13 题：POST 提交 + 检查服务器收到的内容 ----------------   
标题("第 13 题：POST 提交")
# 要求：POST https://httpbin.org/post，json body 是
#       {"product": "鼠标", "price": 99, "stock": 50}
#       从响应里取出服务器收到的 json（键是 "json"），存入变量 echo
#       打印 echo["price"] 和它的类型
#
# echo = None   # ← 删掉这行，自己写
r = requests.post("https://httpbin.org/post",json={"product": "鼠标", "price": 99, "stock": 50},timeout=10)
echo = r.json()["json"]
print(echo["price"],type(echo["price"]).__name__)


# --- 第 14 题：安全网络函数（带异常处理） ----------------------
标题("第 14 题：安全获取函数")
# 要求：定义函数 safe_fetch(url)
#       功能：GET 请求 url，timeout=5，成功返回 r.json()
#             任何网络异常都返回 None，并打印提示
#       用这个函数获取 https://jsonplaceholder.typicode.com/todos/1
#       把返回结果的 "title" 存入变量 todo_title，打印出来
#
# def safe_fetch(url):
#     pass    # ← 删掉 pass，自己写
#
# todo_title = None   # ← 删掉，自己写调用
def safe_fetch(url):
    try:
        r = requests.get(url,timeout=10)
        r.raise_for_status()
        todo_title = r.json()["title"]
        print(todo_title)
    except requests.RequestException:
        return None
        print("requests error!")
safe_fetch("https://jsonplaceholder.typicode.com/todos/1234")
safe_fetch("https://jsonplaceholder.typicode.com/todos/1")

# --- 第 15 题：筛选 API 返回的列表 ----------------------------
标题("第 15 题：筛选 + 提取字段")
# 要求：GET https://jsonplaceholder.typicode.com/todos
#       （返回 200 条待办事项）
#       用推导式筛选出 completed == True 的条目
#       再从中提取每条的 "title"，存入列表 done_titles
#       打印 done_titles 的前 3 个
#
# done_titles = []   # ← 删掉，自己写
try:
        r = requests.get("https://jsonplaceholder.typicode.com/todos",timeout=10)
        r.raise_for_status()
        done_titles = [n["title"] for n in r.json() if n["completed"] == True]
        for i in range(0,3):
            i += 1
            print(done_titles[i])
except requests.RequestException:
        print("requests error!")

# --- 挑战题：综合实战（API → 筛选 → 存本地） -------------------
标题("挑战题：拉取 → 筛选 → 存盘")
# 背景：模拟"从 API 拉取员工列表，筛选出在职的，备份到本地"
#
# 要求分三步：
#   ① GET https://jsonplaceholder.typicode.com/users
#      （返回 10 个用户，每个有 id/name/username/email/company 等字段）
#
#   ② 推导式筛选：只保留 name 里包含字母 "a"（小写）的用户
#      提示：用 "a" in u["name"]，或者 u["name"].lower() 先转小写
#
#   ③ 把筛选后的列表存到本地文件 active_users.json
#      （json.dump，ensure_ascii=False，indent=2）
#
#   ④ 打印：共 X 个用户，其中 N 个名字含 'a'
#      存入变量 total_count 和 filtered_count
#
# total_count = 0      # ← 删掉，自己写
# filtered_count = 0   # ← 删掉，自己写


# ============================================================
# 自测区：全部完成后取消注释，运行无输出 = 全对
# ============================================================
# assert username == "Bret"
# assert echo == {"product": "鼠标", "price": 99, "stock": 50}
# assert isinstance(todo_title, str) and len(todo_title) > 0
# assert len(done_titles) > 0 and isinstance(done_titles[0], str)
# assert total_count == 10
# assert filtered_count > 0 and filtered_count < 10
# import os; assert os.path.exists("active_users.json")
# print("第 8 课测试全部通过！")
