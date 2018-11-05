#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-14 20:26:07
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

from pyecharts import Bar

bar = Bar("图表1", "副标题")
bar.use_theme('dark')  # 使用主题
bar.add("服装", ["衬衫", "羊毛衫", "毛衣", "裤子", "高跟鞋", "袜子"],
        [5, 20, 36, 10, 75, 90], is_more_utils=True)
bar.render(path='demo1.png')
