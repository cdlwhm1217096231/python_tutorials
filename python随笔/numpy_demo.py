#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-01 22:37:54
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np

# ndarray、Numpy数组都指的是ndarray对象

# 创建数组最简单的方法就是使用array函数，下面例子就是将列表转化为数组
data1 = [6, 7.1, 3, 5, 0, 1]
arr1 = np.array(data1)
print(arr1)
# 嵌套序列：由一组等长列表组成的列表   嵌套序列转化为多维数组
data2 = [[1, 0, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print('最小的维度:', arr2.ndim)
print('多维数组大小:', arr2.shape)
print('多维数组的数据类型', arr1.dtype)
# 除了np.array外，还有一些函数可以创建多维数组
print('全0的数组:\n', np.zeros(10))
print('全0的多维数组:\n', np.zeros((2, 3)))
print('全1的数组:\n', np.ones(3))
print('全1的多维数组:\n', np.ones((3, 4)))
print('创建一个没有具体值的数组:\n', np.empty((2, 3, 2)))
print('创建对角数组:\n', np.eye(3, 4))
print('创建单位数组:\n', np.identity(5))
# arange()函数是python中内置函数range的数组版
arr3 = np.arange(10)
print(arr3)
# 指定数组中元素的数据类型
arr1 = np.array([1, 2, 3], dtype=float)
print('验证结果:', arr1.dtype)
# 利用astype方法显式转化其数据类型
arr2 = np.array([1, 2, 3, 4, 5])
print('原数组类型：', arr2.dtype)
float_arr2 = arr2.astype(float)
print('修改后的数组类型：', float_arr2.dtype)
# float转化为int时，自动截断
arr3 = np.array([3.4, -9.8, 34.8, 3.63])
print('原数组类型：', arr3.dtype)
int_arr3 = arr3.astype(int)
print('修改后的数组类型：', int_arr3.dtype)
print('修改后的数组：', int_arr3)
# 字符串转化为数值数组
string_arr4 = np.array(['2.3', '-5.67', '6.75', '-34.8'], dtype=np.string_)
string_arr4.astype(float)
print(string_arr4)
# 数组与标量之间的计算
# 1、大小相等的数组之间的任何算术运算都会映射到元素上
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('原数组:\n', arr)
print('数组之间的计算:\n', arr * arr)
print(arr - arr)
# 2、数组与标量之间的运算
print('数组与标量之间的计算:\n', arr * 0.5)
# 数组重塑 ----使用reshape()方法传入一个表示新形状的元组(通常将一维数组变为多维数组)
arr1 = np.arange(8)
print('原数组:\n', arr1)
print('新数组:\n', arr1.reshape((4, 2)))
print('多维数组也可以被重塑:\n', arr1.reshape((4, 2)).reshape((2, 4)))
# 表示形状的参数中有一维可以是-1，表示该维度的大小由数组本身推断而来
arr2 = np.arange(15)
print('新数组:\n', arr2.reshape((5, -1)))
# 由于shape()本身是一个元组，因此也可以被传入reshape中
other_arr = np.ones((3, 5))
print('other_arr数组的形状:', other_arr.shape)
print('other_arr数组形状重塑:\n', other_arr.reshape(other_arr.shape))

# flatten() ravel()扁平化或散开处理:将多维数组转化为一维数组
arr = np.arange(15)
print('数组重塑:\n', arr.reshape((5, 3)))
print('数组散开操作:', arr.ravel())   # ravel()不会产生源数据的副本
print('数组散开操作:', arr.flatten())  # flatten()总是返回数据的副本
# C和F顺序
"""
C顺序  先经过更高的维度（轴1会优先于轴0被处理）轴1--行方向
表示按照行优先顺序创建数组，每行中的数据被存放在相邻内存的位置上（Numpy数组按照行优先顺序创建）
F顺序  后经过更高的维度（轴0会优先于轴1被处理）轴0--列方向
表示按照列优先顺序创建数组，每列中的数据被存放在相邻内存的位置上
"""
arr = np.arange(12).reshape(3, 4)
print('原数组:\n', arr)
print('按行优先顺序排列:\n', arr.ravel())
print('按列优先顺序排列:\n', arr.ravel('F'))
# 数组的合并与拆分
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr2 = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])
print('数组合并方式1:\n', np.concatenate([arr1, arr2], axis=0))
print('数组合并方式2:\n', np.concatenate([arr1, arr2], axis=1))
# 常见的连接操作vstack、hstack
print('vstack行优先拼接操作(竖直堆叠):\n', np.vstack((arr1, arr2)))
print('hstack列优先拼接操作（水平堆叠）:\n', np.hstack((arr1, arr2)))
# 将数组沿指定轴切分为多个数组
from numpy.random import randn

arr = randn(5, 2)  # 随机数组
print('随机数组:\n', arr)
b = np.split(arr, [1, 3])
print('b:\n', b)
# 元素的重复操作tile repeat
# repeat会将数组中的每个元素重复一定的次数，从而产生一个更大的数组
arr = np.arange(3)
print('数组中的每个元素重复相同次数:', arr.repeat(3))
# 传入一组整数，各个元素可以重复不同次数
arr = np.arange(3)
print('数组中每个元素重复不同次数:', arr.repeat([2, 3, 4]))
# 多维数组沿不同轴重复
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('沿指定轴每个元素重复相同次数:', arr.repeat(2, axis=0))
print('沿指定轴每个元素重复不同次数:', arr.repeat([2, 3], axis=0))
# tile沿指定轴向堆叠数组
arr = randn(2, 2)
print('随机矩阵:\n', arr)
print(np.tile(arr, 2))  # 第二个参数是铺设瓷砖的数量
# 对于标量，瓷砖是水平铺设的
arr = np.array([[1, 2], [3, 4]])
print('元组铺设的布局表示:\n', np.tile(arr, (3, 2)))

# 广播 -- 不同形状数组之间的算术运算执行方式
"""
# 广播原则

如果两个数组的后缘维度（trailing dimension，即从末尾开始算起的维度）的轴长度相符，或其中的一方的长度为1，则认为它们是广播兼容的。广播会在缺失和（或）长度为1的维度上进行。
广播主要发生在两种情况:一种是两个数组的维数不相等，但是它们的后缘维度的轴长相符;另外一种是有一方的长度为1。
"""
# 1、将标量与数组合并时会产生最简单的广播

arr = np.arange(5)
print('最简单广播:', arr * 4)
# 2、数组维度不同，后缘维度的轴长相符,见广播原理.png
arr1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
print('arr1形状', arr1.shape)
arr2 = np.array([1, 2, 3])
print('arr2形状', arr2.shape)
print('arr1 + arr2:\n', arr1 + arr2)
"""
上例中arr1的shape为（4,3），arr2的shape为（3，）。可以说前者是二维的，而后者是一维的。
但是它们的后缘维度相等，arr1的第二维长度为3，和arr2的维度相同
arr1和arr2的shape并不一样，但是它们可以执行相加操作，这就是通过广播完成的，在这个例子当中是将arr2沿着0轴进行扩展
另外的例子,见广播原理1.png
 （3,4,2）和（4,2）的维度是不相同的，前者为3维，后者为2维。但是它们后缘维度的轴长相同，都为（4,2），所以可以沿着0轴进行广播。
"""

# 3.数组维度相同，其中有个轴为1
"""
arr1的shape为（4,3），arr2的shape为（4,1），它们都是二维的，
但是第二个数组在轴1上的长度为1，所以，可以在轴1上面进行广播
具体见图片---广播原理3.png
"""
arr1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
print('arr1形状', arr1.shape)
arr2 = np.array([[1], [2], [3], [4]])
print('arr2形状', arr2.shape)
print('arr1 + arr2:\n', arr1 + arr2)
# 通用函数：快速的元素级数组函数
arr = np.arange(10)
print('arr的平方根:\n', np.sqrt(arr))
print('arr以e为底的指数:\n', np.exp(arr))

x = randn(8)
y = randn(8)
print('x, y中的最大值:\n', np.maximum(x, y))
# floor()函数  --- 小于等于该值的最大整数
# ceil()函数 --- 大于等于该值的最小整数
# 将条件逻辑表述为数组运算
xarry = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarry = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond, xarry, yarry)  # cond=True 选择xarry;否则选择yarry
print(result)
arr = randn(4, 4)
print(np.where(arr > 0, 2, -2))
print('将大于0的元素置为2，小于0的元素不变:\n', np.where(arr > 0, 2, arr))
# 用于布尔型数组的方法
arr = np.array([1, 2, 3, 4, -3, -9, 934])
print('sum()方法用来对布尔数组中的True值计数:', (arr > 0).sum())
# 排序
arr = randn(8)
print('数组排序:', np.sort(arr))
# 多维数组排序
arr = randn(5, 3)
print('原数组:\n', arr)
print('沿轴1方向排序:\n', np.sort(arr, axis=1))
# 数组的唯一化
arr = np.array([1, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6])
print('数组的唯一化:\n', np.unique(arr))
# 等价于下面的代码
print('数组的唯一化:\n', sorted(set(arr)))
# 线性代数
# 矩阵乘法
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 23], [-1, 7], [8, 9]])
print('矩阵乘法:\n', np.dot(x, y))
