#!/usr/bin/env python
#-*- coding：utf-8 -*-
# @Time    ：2018/11/6 21:43
# @Author  ：SunWang
# @File    ：demonCalculator.py

# a + b + c + d + e
def add(string):
    total = 0
    numbers = []
    numbers += string.split("+")
    for num in numbers:
        total += int(num.strip())
    print("{0} = {1}".format(string,total))

# a - b - c - d - e
def reduce(string):
    result = 0
    numbers = []
    numbers +=string.split("-").strip()
    result = int(numbers[0])
    numbers.pop(0)
    for num in numbers:
        result -= num
    print("{0} = {1}".format(string, result))

def ride(string):
    total = 1
    numbers = []
    numbers +=string.split("*")
    for num in numbers:
        total *= int(num.strip())
    print("{0} = {1}".format(string, total))

def division(string):
    result = 0
    numbers = []
    numbers += string.split("/").strip()
    result = numbers[0]
    for num in numbers:
        result /= int(num)
    print("{0} = {1}".format(string, result))


if __name__ == '__main__':
    print("######################################################")
    print("############欢迎来到计算器工作中心#######################")
    print("######################################################")
    print("1： 加法: a + b + c + d + ... ")
    print("2： 减法: a - b - c - d - ...")
    print("3： 乘法: a * b * c * d * ...")
    print("4： 除法: a / b / c / d / ...")
    method = input("Please input a number(1/2/3/4): ")
    str = input("请输入您最终的表达式：")
    if method == 1:
        print("例子: a + b + c + d")
        str = input("###: ")
#20181106d