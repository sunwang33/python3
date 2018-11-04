#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/3 19:06
# @Author  ：SunWang
# @File    ：demon2.py

#整型  int
# a = 10
# print(a)
# print a       python2支持

#布尔类型 bool  True  False
#>= 1  True
#<=0   False

#浮点型   float
# a = 3.141592653
# m = round(a , 2)
# print(m)

#字符串  str 'abc' "abc"  '''abc'''
# string = 'abacdaefaghaiagah'
# print(string)

#find
# result = string.find('def')
# print(result)
# print(string[:])

#replace  替换
# print(string.replace('a','AAA'))

#split  分隔符
# print(string.split('a'))
#结果：['', 'b', 'cd', 'ef', 'gh', 'i', 'g', 'h']

#strip  去除字符串左右空格
string = '  abacdaefaghaiagah  '
print(string.strip())

#字符串打印
print ("my string is : %s " %string )
string1 = 123
string2 = 456
print ("my string is {0}, {1} ,{2} ".format(string,string1,string2)) #推荐

#字符串拼接
print("hel"+"lo")
#结果:hello

#join(可迭代的对象)  #一般是一个list
# newList = string.strip().split('a')
# print(" ### ".join(newList))
#结果：### b ### cd ### ef ### gh ### i ### g ### h









