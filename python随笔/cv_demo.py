#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

path = 'image.jpg'
image = cv2.imread(path)
cv2.imshow("original", image)  # 显示指定路径的图片
cv2.waitKey(0)  # 按键检测，当按键按下时才往下执行
cv2.destroyAllWindows()  # 按键按下后，销毁所有的窗口

# 检测图像的类型
path = 'image.jpg'
image = cv2.imread(path)
print(type(image))  # 查看数据类型
print(image.shape)  # 查看具体的信息
# 在图像上输出文本
path = 'image.jpg'
image = cv2.imread(path)
x, y = 200, 40  # 指定添加文本信息的位置坐标
cv2.putText(img=image, text='lena jpg', org=(x, y), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255))
cv2.imshow('add text a image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 图像大小的调整
img = cv2.imread('image.jpg')
cv2.imshow("src", img)
height, width = img.shape[:2]
# 缩小图像
size = (int(width*0.3), int(height*0.5))
shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
cv2.imshow("shrink", shrink)
# 放大图片
enlarge = cv2.resize(img, (0, 0), fx=1.6, fy=1.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("enlarge", enlarge)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 图像的旋转
path = 'image.jpg'
image = cv2.imread(path)
cols, rows = image.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 10, 0.4)
new_image = cv2.warpAffine(image, M, (rows, cols))
cv2.imshow('raw_image', image)
cv2.imshow('new_image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 图像镜像
path = 'image.jpg'
image = cv2.imread(path)
rows = image.shape[0]
cols = image.shape[1]
mirror_col = int(cols/2)
for col in range(mirror_col):
    image[:, col, :] = image[:, cols-1-col, :]
cv2.imshow('syn_image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 图像的灰度转换
path = 'image.jpg'
image = cv2.imread(path)
cvt_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('cvtColor image', cvt_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


