import sys
sys.path.append("../")
from Utilities.Graph import Graph, DiGraph
from Utilities.ReadGraphExample import GraphCreator



def dp_longest_path(G: Graph, is_vertex_red: dict, target: int) -> int:
    M = [-1] * G.number_of_vertices

    M[0] = is_vertex_red[0]

    #print(is_vertex_red)
    for idx1, vertex1 in enumerate(G):
        #print(idx1, vertex1)
        for vertex2 in vertex1.keys():
            #print(vertex2)
            M[vertex2] = max(M[idx1] + is_vertex_red[idx1],
                                M[vertex2])
    
    return M[target]



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

        G_many = GraphCreator(path)
        target = G_many.index_of_vertex[G_many.target]
        #print(G_many.G)
        #print(G_many.is_vertex_red)
        red_check = {G_many.index_of_vertex[vertex_name]:(1 if v == 1 else 0) for vertex_name,v in G_many.is_vertex_red.items()}


        #print(red_check[0])
        #print("TEST")
        res = dp_longest_path(G=G_many.G, is_vertex_red=red_check, target=target)
        print(res)

    return


if __name__ == "__main__":
    main()
