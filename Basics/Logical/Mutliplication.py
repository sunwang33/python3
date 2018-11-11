#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/11 11:15
# @Author  ：SunWang
# @File    ：Mutliplication.py

# 1 * 1 = 1
# 1 * 2 = 2 2 * 2 = 4
# 1 * 3 = 3 2 * 3 = 6 3 * 3 =9

'''
for i in range(1, 10):  #每一行都以1开头；
    for j in range(1, i+1):  #每一行都以行号结尾；
        print("{0} x {1} = {2} ".format(j, i, j*i), end="") #取消自动换行；
        if j == i:               #当行号等于列号时，才换行。
            print("")
'''

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0} x {1} = {2} ".format(j , i , j*i), end="")
        if j == i :
            print("")
