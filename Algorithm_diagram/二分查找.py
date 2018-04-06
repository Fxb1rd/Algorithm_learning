#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-11 17:20:15
# @Author  : fxb1rd (w1589534127@outlook.com)
# @Link    : http://
# @Version : $Id$

#只适用于有序列表

def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low<=high:
        mid = (low + high)
        guess = list[mid]#取得元素

        if guess == item:
            return mid #返回序号
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None #未找到元素

my_list = [2,4,5,6,8,9]

print(binary_search(my_list,6))
print(binary_search(my_list,10))