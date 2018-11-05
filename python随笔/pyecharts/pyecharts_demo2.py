#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-14 21:48:54
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment


bar = Bar("图表2", "标题2")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
line = Line("图表2", "标题2")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
         [5, 20, 36, 10, 75, 90])
env = create_default_environment("html")
env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')
