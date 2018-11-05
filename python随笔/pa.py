#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-14 23:24:15
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import pandas as pd
import numpy as np


index = pd.Index(data=['Tom', 'Bob', 'Mary', 'James'], name='name')
data = {
    'age': [18, 30, 45, 32],
    'city': ['beijing', 'shanghai', 'nanjing', 'hangzhou'],
    'sex': ['male', 'male', 'female', 'male']
}
user_info = pd.DataFrame(data=data, index=index)
print(user_info)
print('--------------------分隔线1------------------')
print(user_info.info())
