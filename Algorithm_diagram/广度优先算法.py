#!/usr/bin/python 3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-13 11:48:15
# @Author  : fxb1rd (w1589534127@outlook.com)

from collections import deque

#####################关系图（散列表）
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
#################################
def is_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] #检查过的数组
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(person + " is a mango seller!")
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")