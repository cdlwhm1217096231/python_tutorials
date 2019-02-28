#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 17:41:10
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 问题:怎么从一个集合中获得最大或最小的N个元素组成的列表
# 解决方法: heapq模块有两个函数(nlargest()和nsmallest())可以解决上述问题

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 43, 37, 2]
print(heapq.nlargest(3, nums))   # 从nums中找出前3个最大的数
print(heapq.nsmallest(3, nums))

# 两个函数都能接受一个关键字参数，可以用于更加复杂的数据结构
records = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 673.2},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'THU', 'shares': 342, 'price': 45.22},
    {'name': 'ALBABA', 'shares': 554, 'price': 91.02},
]
cheap = heapq.nsmallest(
    3, records, key=lambda s: s['price'])  # key就是接受的一个关键字参数
expensive = heapq.nlargest(3, records, key=lambda s: s['price'])
print('cheap =', cheap)
print('expensive =', expensive)


# 讨论
"""
想在一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量，那么这些函数提供了很好的性能。 因为在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中：
"""
heap = list(nums)
heapq.heapify(heap)  # 将list转化为heap数据结构
print(heap)
"""
堆数据结构最重要的特征是 heap[0] 永远是最小的元素。并且剩余的元素可以很容易的通过调用 heapq.heappop() 方法得到， 该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是 O(log N)，N 是堆大小）
"""
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
"""
当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的。 如果你仅仅想查找唯一的最小或最大（N=1）的元素的话，那么使用 min() 和 max() 函数会更快些。 类似的，如果 N 的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点 （ sorted(items)[:N] 或者是 sorted(items)[-N:] ）。 需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势 （如果 N 快接近集合大小了，那么使用排序操作会更好些）
"""
