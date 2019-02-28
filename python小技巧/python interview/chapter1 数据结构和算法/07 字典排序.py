#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 10:00:20
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


# 问题:创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
# 解决方法: 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类,在迭代操作的时候它会保持元素被插入时的顺序.
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['haha'] = 2
d['niux'] = 3
for key in d:
    print(key, '--->', d[key])
# 想要构建一个将来需要序列化或编码成其他格式的映射的时候， OrderedDict 是非常有用的
import json

j_d = json.dumps(d)   # json格式
print(j_d)
