
from GraphTraversal.BFS import BFS
from Utilities.ReadGraphExample import NoneGraphCreator, AlternateGraphCreator, GraphCreator, FewGraphCreator
from Utilities.Graph import Graph, DiGraph
from Utilities.isDag import is_dag
from Utilities.Dijkstra import dijkstra
from Utilities.DP_max_red import dp_max_reds


import math
from typing import Union


def none(file_path: str) -> int:
    none_data = NoneGraphCreator(file_path)

    G_none = none_data.G
    source = none_data.source_idx
    target = none_data.target_idx

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
    many_data = GraphCreator(file_path)
    name_to_idx = many_data.index_of_vertex 
    target_idx = name_to_idx[many_data.target]

    many_data.add_edges()

    #Only do dp in case of a DAG
    if is_dag(many_data.G):
        #TODO: create this type of dict directly in GraphCreator
        #Convert from dict{vertex_name: red_status} to dict{vertex_idx: red_status}
        red_check = {name_to_idx[vertex_name]:(1 if v == 1 else 0) for vertex_name,v in many_data.is_vertex_red.items()}    

        longest_path = dp_max_reds(G=many_data.G, is_vertex_red=red_check, target=target_idx)

        return longest_path #dp_longest_path(G)

    return "?!"


def few(file_path: str) -> int:
    few_data = FewGraphCreator(file_path)

    #Convert from dict{vertex_name: red_status} to dict{vertex_idx: red_status}
    red_check = {few_data.index_of_vertex[vertex_name]:(1 if v == 1 else 0) for vertex_name,v in few_data.is_vertex_red.items()}    

    source = few_data.source_idx
    target = few_data.target_idx
    
    dist_to_target = dijkstra(G=few_data.G, 
                                is_vertex_red=red_check,
                                source=source,
                                target=target)

    res = math.floor(dist_to_target / 10**7)  # divide by red vertex weight

    return res


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
                    "wall-n-10000.txt"
                ]

    for file_name in grap_files:
        print(file_name)
        path = f"./data/Graphs/{file_name}"

        print("none:", none(path)) #DONE 

        print("many:", many(path)) #INCOMPLETE

        print("alternate:", alternate(path)) #DONE
    
        print("Few:", few(path))


        print()

    return


if __name__ == "__main__":
    main()