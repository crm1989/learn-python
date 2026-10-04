# -*- coding: utf-8 -*-
# ============================================================
# 第 8 课 · AI 应用篇（1）：第三方库、HTTP 请求与 API
# ------------------------------------------------------------
# 前 7 课我们一直在和"自己电脑"打交道：文件、函数、对象。
# 从这一课开始，程序要和"外面的世界"对话了——
# 第 9 课调用大模型，本质上就是今天学的：发一个 JSON，收一个 JSON。
#
# 本课 9 个知识点：
#   1. 第三方库是什么 + pip 安装（requests 已装好）
#   2. venv 虚拟环境（看懂概念，命令动手做一次）
#   3. API 是什么（用 ABAP RFC / 餐厅点菜来类比）
#   4. 第一个 GET 请求，Response 三件套
#   5. GET 带参数 params（有一个"数字变字符串"的坑）
#   6. POST 请求 + JSON 请求体（大模型 API 用的就是它）
#   7. HTTP 状态码（200/404/401/500）+ 请求头 headers
#   8. 网络异常处理：超时、断网时程序不能崩
#   9. 综合实战：网上拉数据 → 筛选 → 存成本地 json
#
# 注意：本课要联网。断网了也别怕，每个示例都包了 try/except，
#       脚本会完整跑完，只是打印"网络请求失败"的提示。
# ============================================================

import json
import requests   # 第三方库，已用 pip install requests 装好


def 标题(序号, 名字):
    print("\n" + "=" * 56)
    print(f"知识点 {序号}：{名字}")
    print("=" * 56)


# ------------------------------------------------------------
# 知识点 1：第三方库 + pip
# ------------------------------------------------------------
标题(1, "第三方库与 pip 包管理器")

# Python 的库分两种：
#   ① 标准库：随 Python 自带，import 就能用（前几课的 json/os/datetime）
#   ② 第三方库：全球开发者发布的工具，要先"安装"才能 import（如 requests）
#
# 安装命令（在【终端】里执行，不是写在代码里）：
#   py -m pip install requests
#
# 国内下载慢，用清华镜像（在命令后加 -i 参数）：
#   py -m pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
#
# 常用 pip 命令三连：
#   py -m pip list              查看已安装的所有库
#   py -m pip install 库名       安装
#   py -m pip uninstall 库名     卸载
#
# requests 已经装好了（2.34.2），所以这行能成功：
print("requests 版本：", requests.__version__)


# ------------------------------------------------------------
# 知识点 2：venv 虚拟环境（概念课，命令在终端动手做）
# ------------------------------------------------------------
标题(2, "venv 虚拟环境是什么")

# 问题场景：项目 A 需要 requests 2.x，项目 B 将来需要 requests 3.x，
# 全装在一个 Python 里会打架。虚拟环境就是给每个项目一个"独立工具箱"。
#
# 类比：SAP 不同项目用各自的客户端配置，互不干扰。
#
# 在终端执行的三条命令（【动手做一次】，做完不影响本讲义运行）：
#
#   ① 在项目文件夹创建虚拟环境（会生成一个 .venv 文件夹）：
#        py -m venv .venv
#
#   ② 激活它（激活后终端提示符最前面会出现 (.venv)）：
#        .venv\Scripts\Activate.ps1
#        （如果提示"禁止运行脚本"，先执行：
#          Set-ExecutionPolicy -Scope CurrentUser RemoteSigned，输入 Y）
#
#   ③ 激活后再 pip install，库就装进这个项目专属的工具箱：
#        py -m pip install requests
#
#   退出虚拟环境：deactivate
#
# 现在阶段你可以暂时不建 venv（全局安装足够学习用），
# 等第 12 课做正式项目时我们再规范使用。知道"它是干嘛的"即可。
print("虚拟环境 = 每个项目独立的第三方库工具箱，避免版本打架")


# ------------------------------------------------------------
# 知识点 3：API 是什么
# ------------------------------------------------------------
标题(3, "API：程序和程序之间的菜单")

# API（应用程序接口）你可以理解为"服务器对外开放的一份菜单"：
#   - 菜单上每一道菜 = 一个功能（查天气、下单、问大模型……）
#   - 你按菜单格式"点菜"（发请求）= HTTP Request
#   - 厨房做好端给你（返回数据）= HTTP Response，通常是 JSON
#
# 你做 SAP 顾问一定熟悉 RFC/BAPI：外部系统按规定参数调用 SAP 的功能。
# Web API 是一回事，只是"通话语言"换成了 HTTP + JSON。
#
# 一次 HTTP 对话的两个主角：
#   请求 Request：  你 → 服务器（要去哪、带什么参数、身份是谁）
#   响应 Response： 服务器 → 你（状态码 + 返回的数据）
print("请求 = 按菜单点菜，响应 = 服务员端菜上桌（通常是 JSON）")


# ------------------------------------------------------------
# 知识点 4：第一个 GET 请求 + Response 三件套
# ------------------------------------------------------------
标题(4, "GET 请求与 Response 三件套")

# 今天用的练习网站：jsonplaceholder.typicode.com
# 它是免费的"假数据服务器"，专门给初学者练手，不用注册、不要 Key。
try:
    响应 = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)

    # Response 对象三件套：
    # ① status_code：状态码（200 = 成功）
    print("① 状态码 status_code =", 响应.status_code)

    # ② text：响应的原始文本（字符串）
    print("② 原文 text 的前 60 个字符：", 响应.text[:60].replace("\n", " "))

    # ③ json()：把 JSON 文本自动转成 Python 字典/列表（第 6 课的反序列化）
    数据 = 响应.json()
    print("③ json() 转换后的类型 =", type(数据).__name__)
    print("   取字段：id =", 数据["id"], "，userId =", 数据["userId"])
except requests.RequestException as e:
    print("网络请求失败（断网或超时）：", type(e).__name__)


# ------------------------------------------------------------
# 知识点 5：GET 带参数 params（注意"数字变字符串"）
# ------------------------------------------------------------
标题(5, "GET 的查询参数 params")

# URL 后面 ?key=value&key=value 的部分叫"查询参数"。
# 不要自己手拼字符串！用 params=字典，requests 帮你拼，还能正确处理中文编码。
try:
    响应 = requests.get(
        "https://httpbin.org/get",          # httpbin 会把收到的请求原样回显
        params={"name": "小明", "age": 18},
        timeout=10,
    )
    print("实际请求的完整网址：")
    print("  ", 响应.url)
    回显 = 响应.json()
    print("服务器收到的参数 args：", 回显["args"])
    # 注意看输出：age 传进去时是数字 18，回来时变成了 '18'（字符串）！
    # 原因：URL 参数本质是网址文本，没有类型之分，所有值都是字符串。
    # 需要数字时，自己 int(回显["args"]["age"]) 转回来。
except requests.RequestException as e:
    print("网络请求失败：", type(e).__name__)


# ------------------------------------------------------------
# 知识点 6：POST + JSON 请求体（重点！大模型 API 就是这种）
# ------------------------------------------------------------
标题(6, "POST 请求与 JSON 请求体")

# GET 像"查菜单"，参数挂在网址上，适合读取数据；
# POST 像"递表格"，数据放在"请求体 body"里发给服务器，适合提交/创建数据。
try:
    账单 = {"item": "午饭", "amount": 25, "category": "餐饮"}
    响应 = requests.post(
        "https://httpbin.org/post",
        json=账单,          # json=字典：自动序列化成 JSON 并放进请求体
        timeout=10,
    )
    收到 = 响应.json()["json"]
    print("服务器收到的 JSON：", 收到)
    print("amount 的类型：", type(收到["amount"]).__name__, "（body 里数字还是数字！）")
    # 对比知识点 5：POST 的 JSON body 保留数据类型，25 仍然是 int。
    # 这就是为什么大模型 API 用 POST——复杂的对话内容、参数都靠 body 传递。
except requests.RequestException as e:
    print("网络请求失败：", type(e).__name__)


# ------------------------------------------------------------
# 知识点 7：状态码与请求头
# ------------------------------------------------------------
标题(7, "HTTP 状态码 + headers 请求头")

# 常见状态码（记住这 4 个，够看懂 90% 的报错）：
#   200  成功
#   401  没带身份/Key 错了（Unauthorized）
#   404  网址或资源不存在（Not Found）
#   500  服务器自己炸了（不是你的锅）
try:
    正常 = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    不存在 = requests.get("https://jsonplaceholder.typicode.com/posts/99999", timeout=10)
    print("存在的资源 →", 正常.status_code)
    print("不存在的资源 →", 不存在.status_code, "（响应体是：", 不存在.text, "）")
except requests.RequestException as e:
    print("网络请求失败：", type(e).__name__)

# headers（请求头）：请求的"附加说明"，最常见两个用途：
#   ① 告诉服务器我要 JSON：      {"Accept": "application/json"}
#   ② 带 API Key 证明身份：      {"Authorization": "Bearer 你的KEY"}
# 第 9 课调用大模型时，Key 就是放在 headers 里的（不是网址里！）。
print("第 9 课的鉴权写法预览：headers={'Authorization': 'Bearer sk-xxxx'}")


# ------------------------------------------------------------
# 知识点 8：网络异常处理（timeout + try/except）
# ------------------------------------------------------------
标题(8, "网络请求的异常处理")

# 网络是不可靠的：断网、超时、服务器宕机都可能发生。
# 两个必备习惯：
#   ① 每次请求都写 timeout=秒数，否则可能永远卡住
#   ② 用 try/except 捕获 requests.RequestException（所有网络异常的总父类）
def 安全获取(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()   # 4xx/5xx 状态码主动抛异常（否则 requests 默认不报错！）
        return r.json()
    except requests.Timeout:
        print("  → 请求超时了")
    except requests.HTTPError as e:
        print(f"  → 服务器返回错误状态码：{e.response.status_code}")
    except requests.RequestException:
        print("  → 网络连不上（检查网络）")
    return None


print("测试正常网址：")
安全获取("https://jsonplaceholder.typicode.com/posts/1")
print("测试错误网址（会触发异常处理，程序不崩）：")
安全获取("https://jsonplaceholder.typicode.com/posts/99999")
安全获取("https://this-domain-does-not-exist-12345.com")


# ------------------------------------------------------------
# 知识点 9：综合实战 —— 网上拉数据，筛选后存到本地
# ------------------------------------------------------------
标题(9, "综合实战：拉取文章 → 筛选 → 存本地 JSON")

# 把今天的 requests + 第 2 课推导式 + 第 6 课 json 存盘串起来：
#   ① 从 API 拉 100 篇文章
#   ② 筛选出 userId == 1 的文章（推导式）
#   ③ 存成本地 posts_backup.json（断网时也能看）
try:
    print("正在从网上拉取文章列表……")
    r = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
    r.raise_for_status()
    全部文章 = r.json()
    print(f"共拉取 {len(全部文章)} 篇")

    # ② 推导式筛选：只保留 userId 为 1 的
    用户1的文章 = [p for p in 全部文章 if p["userId"] == 1]
    print(f"其中 userId=1 的有 {len(用户1的文章)} 篇")
    print("前 3 篇的标题：")
    for p in 用户1的文章[:3]:
        print(f"  #{p['id']} {p['title'][:40]}")

    # ③ 存到本地（第 6 课的 json.dump，中文用 ensure_ascii=False）
    with open("posts_backup.json", "w", encoding="utf-8") as f:
        json.dump(用户1的文章, f, ensure_ascii=False, indent=2)
    print("已备份到 posts_backup.json")
except requests.RequestException:
    print("网络不可用，本次跳过（程序没有崩溃，这就是异常处理的意义）")


# ------------------------------------------------------------
# 本课小结 + 第 9 课预告
# ------------------------------------------------------------
print("\n" + "=" * 56)
print("第 8 课小结")
print("=" * 56)
print("""
1. pip 装第三方库；venv 给每个项目独立工具箱
2. API = 服务器的菜单；请求点菜，响应端菜（JSON）
3. requests.get(网址, params=字典, timeout=10)
4. requests.post(网址, json=字典, timeout=10)  ← 大模型 API 的原型
5. Response 三件套：status_code / text / json()
6. URL 参数全是字符串；JSON body 保留数据类型
7. 状态码：200 成功 / 401 Key问题 / 404 不存在 / 500 服务器炸
8. timeout + try/except + raise_for_status() 是网络请求三件保险
""")
print("第 9 课预告：把 POST 请求的网址换成大模型 API，")
print("body 里放 messages 对话列表，headers 里放 API Key——")
print("你就拥有了一个真正的 AI 聊天机器人。今天学的每一行都会用上。")
