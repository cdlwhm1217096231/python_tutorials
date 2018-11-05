#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-14 21:57:25
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

from pyecharts import Bar
import pandas as pd
import numpy as np


title = "bar chart"
index = pd.date_range('14/9/2018', periods=6, freq='M')
df1 = pd.DataFrame(np.random.randn(6), index=index)
df2 = pd.DataFrame(np.random.randn(6), index=index)

dtvalue1 = [i[0] for i in df1.values]
dtvalue2 = [i[0] for i in df2.values]
_index = [i for i in df1.index.format()]


bar = Bar(title, 'Profit and loss situation')
bar.add('profit', _index, dtvalue1)
bar.add('loss', _index, dtvalue2)
