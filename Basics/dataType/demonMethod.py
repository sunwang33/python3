#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/10 11:53
# @Author  ：SunWang
# @File    ：demonMethod.py

#help()  // ctrl + 鼠标左键
s = "sadfasdfas"
help(s.split)  #split后面跟括号，分割之后是个list。

#dir()
print (dir(s))
#结果：['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

result = s.startswith("sa")
print(result)
#结果：True

#type()
a = '123'
print(type(a))
print(type(int(a)))

#len(s)  //统计字符串的长度。
print(len(s))

#isinstance(a, type)  //返回值是bool类型
print(isinstance(s, str))
#结果：True
print(isinstance(s, dict))
#结果：False

#python 2 print 支持 print s1,s2,s3 就是不回车
#python 3 print 包装成一个函数,print(s, end="")  这个是不回车。

#python 2中存在   xrange() range()  d.iteritems()  d.items()
#python 3中只存在   range()  items()  //取一次数，列一次，效率更高。

#python2  input  输入的必须是整数, raw_input  自动把输入的改成字符串类型
#python3  input  输入的自动转换成字符串类型。

