#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/10 16:52
# @Author  ：SunWang
# @File    ：Factorial.py

def one(n):
    total = 1
    if n == 0:
        total = 1
    else:
        for i in range(1, n+1):
            total *= i
    return total

status = 1
while status:
    result = 0
    n = input("Please input a number(n>=0): ")
    for i in n:
        if i.isdigit():
            print("the number of your input is not a int number.")
            exit()
    #if isinstance(n, int) or n < 0 :
    if int(n) < 0 :
        print("the number of your input is error.")
        break
    for i in range(0, int(n)+1):
        result += one(i)
    print("0! + 1! + ... + n! = {0}".format(result))

#20181110d