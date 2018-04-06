#!/usr/bin/python 3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-13 12:10:24
# @Author  : fxb1rd (w1589534127@outlook.com)

#适用 加权有向无环图 无负权边
#负权边 贝尔曼-福德算法

graph = {}#关系表
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}
######################
infinity = float("inf")#无穷大

costs = {}#开销表
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
#######################
parents = {}#父节点表
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def lowest_cost_path(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:#遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            #如果当前节点开销更低且未经过处理
            lowest_cost = cost#就将其是为开销最低节点
            lowest_cost_node = node
    return lowest_cost_node

node = lowest_cost_path(costs)#在未处理的节点中找到花销最小的节点
while node is not None:#循环在所有节点都被处理后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():#遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:#如果当前节点前往该邻居更近
            costs[n] = new_cost#就更新该邻居的开销
            parents[n] = node#同时将该邻居的父节点设为当前节点
    processed.append(node)#记录处理过的节点
    node = lowest_cost_path(costs)#找到接下来要处理的节点

path = []#路径数组
child = "fin"
while child:#遍历parents散列表
    path.insert(0,child)
    try:
        child = parents[child]
    except:
        break

print(path)
print(costs["fin"])