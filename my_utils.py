# -*- coding: utf-8 -*-
# my_utils.py —— 第 4 课的“自定义模块”演示文件
# 它本身没什么功能，用来演示两件事：
# 1. 别的文件可以 import 它，直接使用里面的函数
# 2. if __name__ == "__main__" 的作用（看 08 讲义的知识点 8）


def shout(text):
    """把文字变成大写并加感叹号（演示用的小函数）"""
    return text.upper() + "！"


def add(a, b):
    """返回两数之和"""
    return a + b


# 这段只在“直接运行本文件”时执行；被别的文件 import 时不执行
if __name__ == "__main__":
    print("这是直接运行 my_utils.py 时的自测输出：")
    print(shout("hello"), add(1, 2))
