#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List
import networkx as nx


VertexID = int
EdgeID = int

class TrailSegmentEntry:
    def __init__(self, v_start, v_end, edge_id, weight):
        self.v_start = v_start
        self.v_end = v_end
        self.edge_id = edge_id
        self.weight = weight

    def __str__(self):
        return f"{self.v_start} -[{self.edge_id}: {self.weight}]-> {self.v_end}"
    
    
Trail = List[TrailSegmentEntry]
def load_multigraph_from_file(filepath: str)-> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.
 
    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """

    G = nx.MultiDiGraph()
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                #pomijanie pustych wierszy
            elements = line.split()
            #rozdzielanie elementów
            if len(elements) >= 3:
                start_node = int(elements[0])
                end_node = int(elements[1])
                lenght = float(elements[2])
                #przypisywanie każdego elementu do innej zmienne
                G.add_edge(start_node, end_node, weight=lenght)
                #dodawanie zapisanych elementów jakko własności krawęzi
    return G

filename = 'data/graph_adjmat.txt'
graph = load_multigraph_from_file(filename)
print("Multigraph edges:")
for edge in graph.edges(data=True):
    print(edge)




def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    trail_elemnets=[]
    min_path= nx.dijkstra_path(g,source=v_start, target=v_end, weight='weight')

    for i in range(len(min_path)-1):
        start_node= min_path[i]
        end_node= min_path[i+1]
        min_weight_edge = None
        for edge in g[start_node][end_node].values():
            if min_weight_edge is None or edge['weight'] < min_weight_edge['weight']:
                min_weight_edge = edge
        edge_id= min_weight_edge['id']
        weight= min_weight_edge['weight']
        trail_elemnets.append(TrailSegmentEntry(start_node,end_node, edge_id, weight))

    return trail_elemnets

G = nx.MultiDiGraph()
G.add_edge(1, 2, weight=0.5, id=1)
G.add_edge(2, 3, weight=0.4, id=2)
G.add_edge(2, 3, weight=0.3, id=3)
G.add_edge(1, 3, weight=1.0, id=4)

v_start = 1
v_end = 3

segments = find_min_trail(G, v_start, v_end)
for segment in segments:
    print(segment)



def trail_to_str(trail):
    if not trail:
        return ""

    result = f"{trail[0].v_start} "
    total_weight = 0.0

    for segment in trail:
        result += f"-[{segment.edge_id}: {segment.weight}]-> {segment.v_end} "
        total_weight += segment.weight

    result += f"(total = {total_weight})"
    return result

str_segments=trail_to_str(segments)
print(str_segments)

