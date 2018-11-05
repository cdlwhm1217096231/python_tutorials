#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dict1 = {'name': 'harden', 'age': 29, 'country': 'American', 'score': 60}
# 访问字典的键值
print("dict1['name'] = ", dict1['name'])
# 修改字典的值
dict1['name'] = 'curry'
print("dict['name'] = ", dict1['name'])
# 删除字典
del dict1['country']
print(dict1)
# 清空字典
dict1.clear()
print(dict1)
dict2 = {'name': 'harden', 'age': 29, 'country': 'American', 'score': 60}
dict3 = {'name': 'curry', 'age': 30, 'country': 'American', 'score': 160}
print(len(dict3))
# 时间和日期
import time, datetime
# 获取当前时间
localtime = time.localtime(time.time())
print('当前时间为: ', localtime)
print('元组类型: ', type(localtime))
# 获取格式化的时间
t = time.localtime()
print('asctime()获取格式化时间: %s' % time.asctime(t))
# 将日期转化为字符串
print('将日期转化为字符串方法1:', time.strftime("%Y-%m-%d %H:%M:%S"))
print('将日期转化为字符串方法2:', datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
print('将日期转化为字符串方法3:', str(datetime.datetime.now())[:19])
# 将字符串转化为日期
ending_time = '2018-07-12 20:35:59'
d = datetime.datetime.strptime(ending_time, "%Y-%m-%d %H:%M:%S")
print('将字符串转化为日期:', d)
# 获取日期差
today = datetime.date.today()
print('今天:', today)
delta_day = datetime.timedelta(days=1)
yesterday = datetime.date.today() - delta_day
print('昨天:', yesterday)
tomorrow = datetime.date.today() + delta_day
print('明天:', tomorrow)
tomorrow_zero_time=datetime.datetime.strftime(tomorrow, '%Y-%m-%d %H:%M:%S')
print('获取明天零点的时间:', tomorrow_zero_time)
# 获取时间差
delta_day = datetime.timedelta(days=1)
today_time = datetime.datetime.now()
print('今天:', datetime.datetime.strftime(today_time, '%Y-%m-%d %H:%M:%S'))
yesterday_time = datetime.datetime.now() - delta_day
print('昨天:', datetime.datetime.strftime(yesterday_time, '%Y-%m-%d %H:%M:%S'))
tomorrow_time = datetime.datetime.now() + delta_day
print('明天:', datetime.datetime.strftime(tomorrow_time, '%Y-%m-%d %H:%M:%S'))
# 字符串日期格式化为秒数
ending_time = '2018-07-12 20:35:59'
d = datetime.datetime.strptime(ending_time,"%Y-%m-%d %H:%M:%S")
time_sec_float = time.mktime(d.timetuple())
print('字符串日期格式化为秒数:', time_sec_float)
# 日期格式化为秒数
d = datetime.datetime.today()
print('日期格式:', d)
time_sec_float = time.mktime(d.timetuple())
print('日期格式化为秒数', time_sec_float)
# 秒数转字符串
time_sec = time.time()
print('秒数:', time_sec)
print('秒数转字符串:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_sec)))