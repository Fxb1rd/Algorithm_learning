#!/usr/bin/python 3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-19 12:30:25
# @Author  : fxb1rd (w1589534127@outlook.com)

#集合覆盖问题
#

#--------------所需覆盖的地区--------------------
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
#将数组转化为集合/集合中不能有重复元素，能进行 |（并集）、&（交集）、-（差集）运算

#-------------电视台散列表------------------------
stations = {}
stations["s_one"] = set(["id","nv","ut"])
stations["s_two"] = set(["wa","id","mt"])
stations["s_three"] = set(["or","nv","ca"])
stations["s_four"] = set(["nv","ut"])
stations["s_five"] = set(["ca","az"])

final_stations = set()#最终选择结果

#--------------------算法---------------
while states_needed:#知道所有地区都覆盖到
    print(states_needed)
    best_station = None #最佳站点
    states_covered = set()
    for station,states in stations.items():#遍历散列表
        covered = states_needed & states#取得未覆盖的地区与电视台地区的交集
        if len(covered) > len(states_covered):#贪婪选择
            best_station = station
            states_covered = covered
    states_needed -= states_covered#去掉已选择的区域
    final_stations.add(best_station)#添加已选择的站点

print(final_stations)

#NP完全问题
#
#动态规划
