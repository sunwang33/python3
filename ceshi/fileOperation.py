#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/11 19:59
# @Author  ：SunWang
# @File    ：fileOperation.py

filename = input("Please input a name of this file('EOF' is quit): ")
file = open(filename , 'w',encoding="utf-8")
while 1:
    fileContext = input("Please  input the context of this file: ")
    if fileContext == "EOF":
        break
    else:
        file.write(fileContext)
        file.write("\n")
file.close()
fileRead = open(filename, 'r',encoding="utf-8")
context2 = fileRead.read()
print("############################")
print(context2)
print("############################")

