from GraphTraversal.BFS import BFS
from Utilities.ReadGraphExample import NoneGraphCreator, AlternateGraphCreator, GraphCreator
from Utilities.Graph import Graph, DiGraph
from Utilities.isDag import is_dag
from DynamicProgramming.DAG_longest_path import dp_longest_path

from typing import Union


def none(file_path: str) -> int:
    none_graph_obj = NoneGraphCreator(file_path)

    G_none = none_graph_obj.G
    source = none_graph_obj.source_idx
    target = none_graph_obj.target_idx

    bfs = BFS(G=G_none, source=source, target=target)

    return bfs._dist_to[target] #default value is -1, which will be printed in case of no s-t path



def some(file_path: str) -> Union[bool, str]:
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


def many(file_path: str) -> Union[bool, str]:
    G_many = GraphCreator(file_path)
    name_to_idx = G_many.index_of_vertex 

    target_idx = name_to_idx[G_many.target]

    
    #Only do dp in case of a DAG
    if is_dag(G_many.G):
        #Convert from dict{vertex_name: red_status} to dict{vertex_idx: red_status}
        red_check = {name_to_idx[vertex_name]:(1 if v == 1 else 0) for vertex_name,v in G_many.is_vertex_red.items()}    

        longest_path = dp_longest_path(G=G_many.G, is_vertex_red=red_check, target=target_idx)

        return longest_path #dp_longest_path(G)

    return "?!"


def few(file_path: str) -> int:
    #G = FewGraphCreator()

    #res = Dijkstra(G)

    return #res


def alternate(file_path: str) -> bool:
    alternate_graph_obj = AlternateGraphCreator(file_path)

    G_alt = alternate_graph_obj.G
    
    source = alternate_graph_obj.source_idx
    target = alternate_graph_obj.target_idx

    bfs = BFS(G=G_alt, source=source, target=target)

    return bfs.has_path_to(target)







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
        path = f"./data/Graphs/{file_name}"

        #print("none:", none(path)) #DONE 

        print("many:", many(path)) #INCOMPLETE

        #print("alternate:", alternate(path)) #DONE
    


        print()

    return


if __name__ == "__main__":
    main()