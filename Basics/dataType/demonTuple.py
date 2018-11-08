#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/8 21:29
# @Author  ：SunWang
# @File    ：demonTuple.py

l =  list()
print(l)

t = tuple()
print(t)
#个人理解list可以进行增删改查，tuple只能查。
a = (1)
print(type(a))
#结果：<class 'int'>
b = (1,)
print(type(b))
#结果：<class 'tuple'>
##注意：在tuple类型中，单个元素一定要加逗号。否则，无法识别是tuple类型。

m = (1, 2, 3, 4, 5, 1, 2, 3, 1, 2)
#count(value)   //统计元素的个数。
#统计1有多少个
print(m.count(1))
#index(value)  //返回第一个value元素的下标。
#返回元素5的下标
print(m.index(5))

