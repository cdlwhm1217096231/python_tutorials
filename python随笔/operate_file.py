#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/17 15:59'
__author__ = 'cdl'

# 读文件
try:
    f = open('demo.txt', 'r')  # 以读的模式打开一个文件对象，即成功地打开了一个文件
    print(f.read())   # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
except IOError as e:
    print('文件不存在！')
finally:
    if f:
        f.close()  # 调用close()方法关闭文件,文件使用完毕后必须关闭
# 简化方法
with open('demo.txt', 'r') as f:   # Python 引入了 with 语句来自动帮我们调用 close() 方法
    print(f.read())  # 调用 read() 会一次性读取文件的全部内容，如果文件有 10G，内存就爆
# readline()----每次读取一行内容
# readlines()----一次读取所有内容并按行返回 list
with open('demo.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
# 读二进制文件
with open('时间元组类型介绍.png', 'rb') as f:
    for line in f.readlines():
        print(line.strip())
# 字符编码----------要读取非UTF-8编码的文本文件，需要给 open() 函数传入 encoding 参数
with open('demo.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
# 写文件----------会清楚文件中已有的内容
f = open('demo.txt', 'w')
f.write('Hello, curry!')
f.close()

with open('demo.txt', 'w') as f:
    f.write('hello, harden!')
# 测试
with open('demo1.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
# 追加模式
with open('demo1.txt', 'a', encoding='utf-8') as f:
        f.write('\nhello，哈登！')
