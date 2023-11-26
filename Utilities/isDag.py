from graphlib import TopologicalSorter

import sys
sys.path.append("../")
from Utilities.Graph import Graph, DiGraph
from Utilities.ReadGraphExample import GraphCreator


def is_dag(G: Graph) -> bool:
    
    g2 = {str(i): set(str(neighbor) for neighbor in neighbors.keys()) for i, neighbors in enumerate(G)}

    try:
        # topological sort the graph
        ts = TopologicalSorter(g2)
        tuple(ts.static_order())
        return True
    except:
        return False



def main():
    grap_files = ["G-ex.txt",
                    "grid-5-0.txt",
                    "increase-n8-1.txt",
                    "P3.txt",
                    "rusty-1-17.txt",
                    "ski-illustration.txt",
                    "wall-n-10000.txt"
                ]

    for file_name in grap_files:
        print(file_name)
        path = f"../data/Graphs/{file_name}"

        G_many = GraphCreator(path)
        G = G_many.G

        print(is_dag(G))


    return


if __name__ == "__main__":
    main()
