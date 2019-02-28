#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 10:11:12
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


# 问题：怎样在字典中执行一些计算操作
price = {
    "banana": 3.23,
    "apple": 2.54,
    "grape": 4.94,
    "peach": 3.65,
}
# 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来
min_price = min(zip(price.values(), price.keys()))
max_price = max(zip(price.values(), price.keys()))
print("min value:", min_price)
print("max value:", max_price)
# 字典数据的排序
sorted_dict = sorted(zip(price.values(), price.keys()))
print(sorted_dict)
# 需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器
price_and_name = zip(price.values(), price.keys())
print(max(price_and_name))
# print(min(price_and_name))

# 如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值
print(max(price))
print(max(price.values()))
print(min(price.values()))
# 在min()和max()函数中提供key函数参数来获取最小值或最大值对应的键的信息
max_value = max(price, key=lambda k: price[k])  # 类似于map函数和pandas中的apply函数
print(max_value, max(price.values()))
min_value = min(price, key=lambda k: price[k])
print(min_value, min(price.values()))
# 需要注意的是在计算操作中使用到了 (值，键) 对。当多个实体拥有相同的值的时候，键会决定返回结果
price = {
    "AAA": 333,
    "ZZZ": 333,
}
max_value = max(zip(price.values(), price.keys()))
print(max_value)
