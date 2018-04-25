# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 11:04
# @Author  : weic
# @FileName: 1.py
# @Software: PyCharm
import numpy as np
a=[1,2,10,11
   ]


for index,num in enumerate(a):
    print(index,num)


b=iter(a)
print(next(b))
print(next(b))
print(next(b))

label=np.asarray(a).reshape(-1,2)
print(label)
print(label[[0],:])