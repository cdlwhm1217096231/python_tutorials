#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-30 13:44:14
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import io
import sys

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
url = 'http://www.sina.com.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
req = requests.get(url, headers=headers)
req.encoding = 'utf-8'
print(req.status_code)
html = req.text
print(html)
print('-------------------------------1---------------------')
doc = pq(html)
a = doc('.tab-cont-out li a')
print(a.text())
print('--------------------------------2--------------------')
a = doc('.mod-045.uni-blk .uni-blk-b li a')
print(a.text())
print('-------------------------------3----------------------')
doc = pq(html)
a = doc('#xy-impcon li a')
print(a.text())
print('-------------------------------4----------------------')

