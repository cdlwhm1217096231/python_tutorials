#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 18:00:15
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


import heapq
# 问题：怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
# 解决方法：利用 heapq 模块实现了一个简单的优先级队列


class PriorityQueue:
    def __init__(self):
        self._queue = []  # 用户自定义的私有变量
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('dana'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
"""
仔细观察可以发现，第一个 pop() 操作返回优先级最高的元素。 另外注意到如果两个有着相同优先级的元素（ foo 和 grok ），pop 操作按照它们被插入到队列的顺序返回的。
"""
