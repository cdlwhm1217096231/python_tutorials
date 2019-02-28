#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 10:21:30
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 问题：怎么实现一个键对应多个值的字典
# 解决方法:一个字典就是一个键对应一个单值的映射。如果想一个键映射成多个值，就需要将这个值放到另外的容器中(如列表或者集合)

d = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
}

e = {
    'c': {34, 56, 32},
    'd': {67, 23, 12},
}
# 如果想保持元素的插入顺序就使用列表；如果想去掉重复元素就使用集合(且不关注元素的顺序)

# 可以使用colletions模块中的defaultdict来构造字典，defaultdict的一个特征是它会自动初始化每个key刚开始对应的值
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
d1 = defaultdict(set)
d1['a'].add(1)
d1['a'].add(2)
d1['b'].add(4)
print(d1)
# defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替
d = {}  # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

# 创建一个多值映射字典是很简单的。但是，如果你选择自己实现的话，那么对于值的初始化可能会有点麻烦
d1 = {"three": 3}
pairs = {"one": 1, "two": [2, 22, 222]}
for key, value in pairs.items():
    if key not in d1:
        d1[key] = value
print(d1)
