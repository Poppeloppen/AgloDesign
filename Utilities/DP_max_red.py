import sys
sys.path.append("../")
from Utilities.Graph import Graph, DiGraph
from Utilities.ReadGraphExample import GraphCreator
from Utilities.isDag import is_dag



def dp_max_reds(G: Graph, is_vertex_red: dict, target: int) -> int:
    M = [-1] * G.number_of_vertices

    M[0] = is_vertex_red[0]

    #print(is_vertex_red)
    for idx1, vertex1 in enumerate(G):
        #print(idx1, vertex1)
        for vertex2 in vertex1.keys():
            #print(vertex2)
            M[vertex2] = max(M[idx1] + is_vertex_red[vertex2],
                                M[vertex2])
    
    return M[target]



def main():
    grap_files = ["G-ex.txt",
                    #"grid-5-0.txt",
                    "increase-n8-1.txt",
                    #"P3.txt",
                    #"rusty-1-17.txt",
                    "ski-illustration.txt",
                    #"wall-n-10000.txt"
                ]

    for file_name in grap_files:
        print(file_name)
        path = f"../data/Graphs/{file_name}"

        G_data = GraphCreator(path)
        G_data.add_edges()

        G = G_data.G

        print("type:", type(G))
        print("is DAG?:", is_dag(G))
        
        
        target_idx = G_data.index_of_vertex[G_data.target]
        print("idx of target:", target_idx)
        
        red_check = {G_data.index_of_vertex[vertex_name]:(1 if v == 1 else 0) for vertex_name,v in G_data.is_vertex_red.items()}


        #print(red_check[0])
        #print("TEST")
        res = dp_max_reds(G=G_data.G, is_vertex_red=red_check, target=target_idx)
        print("max red cnt:", res)

        print()

    return


if __name__ == "__main__":
    main()
