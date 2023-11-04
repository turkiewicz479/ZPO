import networkx as nx
from collections import namedtuple
def load_multigraph_from_file(filepath):

    G = nx.MultiDiGraph()
    with open(filename, 'r') as file:
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
"""
filename = 'data/graph_adjmat.txt'
graph = load_multigraph_from_file(filename)
print("Multigraph edges:")
for edge in graph.edges(data=True):
    print(edge)
"""

TrailSegmentEntry = namedtuple('TrailSegmentEntry', ['v_start', 'v_end', 'edge_id', 'weight'])

def find_min_trail(g, v_start, v_end):
    trail_elemnets=[]
    min_path= nx.dijkstra_path(g,source=v_start, target=v_end, weight='weight')
    result = f"{v_start} "
    total_weight = 0.0
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
        

        result += f"-[{edge_id}: {weight}]-> {end_node} "
        total_weight += weight

    result += f"(total = {total_weight})"

    return result

G = nx.MultiDiGraph()
G.add_edge(1, 2, weight=0.5, id=1)
G.add_edge(2, 3, weight=0.4, id=2)
G.add_edge(2, 3, weight=0.3, id=3)
G.add_edge(1, 3, weight=1.0, id=4)

v_start = 1
v_end = 3

segments = find_min_trail(G, v_start, v_end)
print(segments)
print(nx.dijkstra_path_length(G, v_start, v_end))




