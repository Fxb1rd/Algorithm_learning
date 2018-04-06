#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-11 18:15:45
# @Author  : fxb1rd (w1589534127@outlook.com)
# @Link    : http://
# @Version : $Id$

#D&C模式  递归算法 尾递归

def quicksort(arr):
    if len(arr)<2:
        return arr  #基线条件
    else:
        pivot = arr[0] #递归条件 基准值
        less = [i for i in arr[1:] if i <= pivot]#小于基准值的元素组成的数组
        more = [i for i in arr[1:] if i > pivot]#大于基准值的元素组成的数组
        return quicksort(less) + [pivot] + quicksort(more)

my_list = [3,6,23,5465,54,8,44,35]

print(quicksort(my_list))

