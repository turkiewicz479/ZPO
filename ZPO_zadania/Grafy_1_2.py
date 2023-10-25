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

def is_acyclic(G: Dict[int, List[int]]) -> bool:
    visited = set()  
    # Używamy listy, aby sprwadzić czy odwiedziliśmy dany wierzchołek
    rec_stack = set()  
    # Używamy zbioru do śledzenia rekurencyjnego stosu

    def is_acyclic_util(point):
        #ta funkcja zwraca czy dany ciąg połączeń jest acykliczny sprawdza czy dany element był już odwiedzany oraz czy był odwiedzony w tej rekurencji, 
        #jeżeli na oba pytania odpowiedz brzmi tak to wychodzimy z funkcji i zwracamy flase jeżeli tylko ten elemnet był odwiedzony ale nie wtej rekurencji to rónież wychodzimy z tej funkcji,
        #ale z odpowiedziią true inczej wykonujemy funkcje która dodaje dany element do obydóch zbiorów i sprawdza sąsiadów 
        if point in rec_stack:
            return False
        if point in visited:
            return True

        visited.add(point)
        rec_stack.add(point)

        for neighbor in G.get(point, []):
            if not is_acyclic_util(neighbor):
                return False

        rec_stack.remove(point)
        return True

    for node in G:
        if not is_acyclic_util(node):
            return False

    return True
Lista_sasiedztwa1={1: [2, 3], 3: [4]}
Lista_sasiedztwa2={1: [2], 2: [3], 3: [1]}
Lista_sasiedztwa3={2: [1, 3], 3: [2]}
Lista_sasiedztwa4={1: [2], 3: [2, 4], 4: [3]}
Lista_sasiedztwa5={1: [2, 3], 2: [4], 3: [4]}
Lista_sasiedztwa6={1: [2, 3], 2: [3]}
Lista_sasiedztwa7={1: [2], 2: [3], 3: [1, 4]}
print(is_acyclic(Lista_sasiedztwa1))
print(is_acyclic(Lista_sasiedztwa2))
print(is_acyclic(Lista_sasiedztwa3))
print(is_acyclic(Lista_sasiedztwa4))
print(is_acyclic(Lista_sasiedztwa5))
print(is_acyclic(Lista_sasiedztwa6))
print(is_acyclic(Lista_sasiedztwa7))