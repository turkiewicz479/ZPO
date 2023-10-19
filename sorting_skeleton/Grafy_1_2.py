#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict

def dfs_recursive(G: Dict[int, List[int]], s: int, visited: List[int]=None) -> List[int]:
    if visited is None:
        visited=[]
    if s not in visited:
        visited.append(s)
    for u in G[s]:
        if not u in visited:
            dfs_recursive(G,u,visited)
    return visited

    pass
 
def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stos=[]
    stos.append(s)
    visited=[]
    while stos:
        v=stos.pop()
        if v not in visited:
            visited.append(v)
            for u in G[v][::-1]:
                stos.append(u)
    return visited
            

    pass
G = {
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]
}
list1=dfs_recursive(G,1)
print(list1)
list2=dfs_iterative(G,1)
print(list2)