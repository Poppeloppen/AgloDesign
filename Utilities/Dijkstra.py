from heapq import heappop as pop, heappush as push
import math

import sys
sys.path.append("../")
from Utilities.ReadGraphExample import NoneGraphCreator, AlternateGraphCreator, GraphCreator, FewGraphCreator
from Utilities.Graph import Graph, DiGraph


def dijkstra(G: Graph, is_vertex_red: dict, source: int, target: int) -> int:
    
    dist = [10**18] * G.number_of_vertices

    pq = []

    def add(i, dst):
        if dst < dist[i]:
            dist[i] = dst
            push(pq, (dst, i, is_vertex_red[i]))
    
    add(source, is_vertex_red[source])
    
    while pq:
        dist_to_i, i, red = pop(pq)
        if i == target:
            return dist[target]
        if dist_to_i != dist[i]:
            continue

        for j in G[i].keys():
            add(j, dist_to_i + G[i][j])
    return -1


    
    return






def main():
    grap_files = ["G-ex.txt",
                "grid-5-0.txt",
                "increase-n8-1.txt",
                "P3.txt",
                "rusty-1-17.txt",
                "ski-illustration.txt",
                #"wall-n-10000.txt"
                ]


    for file_name in grap_files:
        print(file_name)
        path = f"../data/Graphs/{file_name}"
        
        G_few = FewGraphCreator(path)
        #print(G_few.G)

        #Convert from dict{vertex_name: red_status} to dict{vertex_idx: red_status}
        red_check = {G_few.index_of_vertex[vertex_name]:(1 if v == 1 else 0) for vertex_name,v in G_few.is_vertex_red.items()}    
        #print(red_check)
        source = G_few.source_idx
        target = G_few.target_idx

        res = Dijkstra(G=G_few.G, is_vertex_red=red_check, source=source, target=target)
        print(res)
        print()
    return


if __name__ == "__main__":
    main()