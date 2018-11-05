#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/31 14:52'
__author__ = 'cdl'

import requests, re

url = 'https://www.zhihu.com/explore'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}
req = requests.get(url=url, headers=headers)
req.encoding = 'utf-8'
print(req.text)
pattern = re.compile('explore-feed.*?<a class="question_link".*?>(.*?)</a>', re.S)
titles = re.findall(pattern, req.text)
for title in titles:
    print(title)

import requests, re

url = 'http://gs.njust.edu.cn/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}
req = requests.get(url=url, headers=headers)
req.encoding = 'utf-8'
pattern = re.compile('class="wp_article_list".*?target="_blank"*?title="(.*?)">.*?', re.S)
titles = re.findall(pattern, req.text)
print(titles)