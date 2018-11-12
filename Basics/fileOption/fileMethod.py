#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/12 21:27
# @Author  ：SunWang
# @File    ：fileMethod.py
import codecs

ENCODING = "utf-8"
f = open("1.log", encoding = ENCODING)  #"当文件还没有的时候，先open。"
print(f.name)
print(f.mode)
print(f.readline())
print(f.readlines())
print(f.readlines())  #第二次读取不到任何内容。
print(f.closed)
f.close()
print(f.closed)

#“有时候我们打开文件，可能会忘记关闭，后来就出现了with用法。”
with open("1.log", "r", encoding = ENCODING ) as f:
    print(f.read())   #执行完这条语句之后，自动关闭。

#通过codecs解决乱码问题。单独写open时，也这么用。
with codecs.open("1.log", "r", encoding = ENCODING ) as f:
    print(f.read())   











