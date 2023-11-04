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
    white = []
    grey = [start_vertex_id]
    black = []
    for i in range(max_distance):
        new_white=[]
        for x in grey:
                #przechodzenie prez kazdy szary element
            if x in adjlist: 
                for y in adjlist[x]:
                    #przechodzenie przez sasiadow kazdego szarego elementu
                    if y not in white and y not in grey and y not in black:
                        new_white.append(y)
                            #jezeli ten element nie jest pomalowany to pomaluj go na biało
                        neig_set.add(y)
                    elif y in white:
                            white.remove(y)
                            grey.append(y)
                    black.extend(grey)
                    grey= new_white
    return set(neig_set)
G = {
    1: [2, 4],
    2: [3],
    4: [5],
    5: [2, 6],
    7: [1]
}
d=2
set1=neighbors(G, 1, d)
print(set1)

                

                

#raise NotImplementedError()