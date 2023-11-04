#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Set, Dict
 
# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int
 
# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]
 
Distance = int
 
def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    neig_set = set()
    kolor={}
    distance = {}
    
    for u in adjlist:
        for v in adjlist[u]:
            kolor[v]=0 #Biały, malowanie każdego elementu do którego można dotrzeć (nie tylko takiego który jest w słowniku)
    kolor[start_vertex_id]=1#Szary
    distance[start_vertex_id] = 0
    Q=[start_vertex_id]

    while Q:
        u=Q.pop(0)
        for v in adjlist.get(u, []):
            if v in kolor and kolor[v]==0:
                kolor[v]=1
                distance[v] = distance[u] + 1
                if distance[v] <= max_distance:
                    neig_set.add(v)
                    Q.append(v)
                     
                 
        kolor[u] = 2#Czarny
    

    return set(neig_set)

"""
G = {
    1: [2, 4],
    2: [3],
    4: [5],
    5: [2, 6],
    7: [1]
}
d=2
set1=neighbors(G, 1, 1)
print(set1)
"""
#raise NotImplementedError()