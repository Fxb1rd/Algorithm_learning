#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-11 17:44:43
# @Author  : fxb1rd (w1589534127@outlook.com)
# @Link    : http://
# @Version : $Id$

def findSmallest(arr) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort(arr):#排序
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

my_list = [3,5,7,2,1,9]

print(select_sort(my_list))
