#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/10 10:44
# @Author  ：SunWang
# @File    ：demonDict.py

#字典的定义：
#1.
d1 = dict(name="ling",age=2)
#2.
d2 = {"id": 10001, "name":"lingxiangxiang"}
#3.
d3 =  dict([("ip", "1.1.1.1"),("address", "beijing")])

print(d1)
print(d2)
print(d3)

#方法
#get(key)   //根据key获取value。
#setdefault   //根据key获取value,如果key不存在，可以设置默认的value。
print(d1.get("name"))
#结果：ling

print(d1.get("address"))
#结果：None

print(d1.setdefault("name"))
#结果：ling

print(d1.setdefault("address","beijing"))
#结果：beijing

print(d2.keys())
#结果：dict_keys(['id', 'name'])
print(type(d2.keys()))
#结果：<class 'dict_keys'>

# for i in d2:
#     print(i)

print(d2.values())
#结果：dict_values([10001, 'lingxiangxiang'])

#python 2中 有items  和iteritems

for x, y in d3.items():  #“items每次给你遍历出两个数。”
    #print(x, y)
    print("key = {0}, value = {1}".format(x, y))

#update  //就跟我们list中的+相似。
#l = list   l +=[1, 2, 3, 4]
# l = list()
# m = [1, 2, 3, 4, 5, 6]
# l += m
# print(l)

m = dict()
n = dict(name = "ling", age = 18)  #“这是从其他地方获取的字典。”
m.update(n)
print(m)
#结果：{'name': 'ling', 'age': 18}

#pop(key)  //删除key所对应的元素，并返回key所对应的value值。
print(d3)
#结果：{'ip': '1.1.1.1', 'address': 'beijing'}
keydelete = d3.pop("ip")
print(keydelete)
#结果:1.1.1.1
print(d3)
#结果：{'address': 'beijing'}

#20181110a