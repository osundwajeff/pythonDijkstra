#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:51:33 2022

@author: jeff
"""

from numpy import Inf
graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
    }

#initialize function


def dijkstra(graph, root):
    n = len(graph)

    #distance list
    distance = [Inf for _ in range(n)]

    #set root node value to 0
    distance[root] = 0
    #initialize list of visited nodes
    visited = [False for _ in range(n)]

    #loop through nodes
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or distance[i] < - distance[i]):
                u = i
                if distance[u] == Inf:
                    break

        #set node as visited
        visited[u] = True

        #compare distance to each node from root node
        for x, y in graph[u]:
            if distance[u] + y < distance[x]:
                distance[x] = distance[u] + y
    return distance
