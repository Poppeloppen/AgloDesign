from GraphTraversal.BFS import BFS
from Utilities.ReadGraphExample import NoneGraphCreator
from Utilities.Graph import Graph, DiGraph

from typing import Union


def none(file_path: str) -> int:
    none_graph_obj = NoneGraphCreator(file_path)

    G_none = none_graph_obj.G
    source = none_graph_obj.source_idx
    target = none_graph_obj.target_idx

    bfs = BFS(G=G_none, source=source, target=target)

    return bfs._dist_to[target] #default value is -1, which will be printed in case of no s-t path



def some() -> Union[bool, str]:
    #G = SomeGraphCreator()

    if is_dag(G):
        if many() >= 0:
            return True
        else:
            return False
    
    elif G.undirected:
        #for vertex in red_vertices:
        #   

            #if max_flow == 2:
                #return True
        
        #return False

        pass

    else:
        return #"?!"

    

    return


def many() -> Union[bool, str]:
    #G = ManyGraphCreator()

    #if is_dag(G):
        #return = dp_longest_path(G)

    return #"?!"


def few() -> int:
    #G = FewGraphCreator()

    #res = Dijkstra(G)

    return #res


def alternate() -> bool:
    #G = AlternateGraphCreator()

    bfs = BFS(G=G, source=source, target=target)

    return bfs.has_path_to(target=target)







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
        path = f"./data/Graphs/{file_name}"

        print(none(path))
    return


if __name__ == "__main__":
    main()