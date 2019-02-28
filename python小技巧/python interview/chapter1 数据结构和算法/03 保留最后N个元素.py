#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 11:54:12
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

from collections import deque
# 问题: 在迭代或者其他操作时，怎么只保留最后有限几个元素的历史记录

# 解决方法:使用的是collections.deque来保存有限的历史记录

"""
使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
"""
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print('q =', q)
q.append(4)
print('q =', q)
q.append(5)
print('q =', q)
"""
也可以手动在一个列表上实现这一的操作（比如增加、删除等等）。但是这里的队列方案会更加优雅并且运行得更快些。
更一般的， deque 类可以被用在任何你只需要一个简单队列数据结构的场合。 如果你不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添加和弹出元素的操作。
"""
qq = deque()
qq.append(11)
qq.append(22)
qq.append(33)
print('qq =', qq)
qq.appendleft(666)
print(qq)
print('弹出操作：', qq.pop())
print('左侧弹出操作:', qq.popleft())
"""
在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N)
"""
