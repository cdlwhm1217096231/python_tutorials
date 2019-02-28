#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 09:35:20
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


# 一般形式 d = {key: value for key, value in 可迭代对象}

dict1 = {"player1": "curry", "player2": "harden", "player3": "James"}
d = {key: value for (key, value) in dict1.items()}  # 字典生成式
print(d)
lis = ["curry", "harden", "James"]
new_lis = [(i, name) for i, name in enumerate(lis)]  # 列表生成式
print(new_lis)


# for i, name in enumerate(lis):
#     new_lis.append
#     print(i, "---->", name)
