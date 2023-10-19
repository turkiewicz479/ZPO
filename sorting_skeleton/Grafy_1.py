#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict
 
def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    
    list_dict={}
    for x in range(len(adjmat)):
        curr_list=[]
        for i in range(len(adjmat[x])):
            for j in range(adjmat[x][i]):
                curr_list.append(i+1)
        #print(curr_list)
        if curr_list:
            list_dict[x+1]=curr_list
    return list_dict
    pass
A = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 2, 0]
]
print(adjmat_to_adjlist(A))
A = [
    [0, 1],
    [0, 0]
]
print(adjmat_to_adjlist(A))
