from Graph import Graph, DiGraph

def ReadGraphExample(file_path: str) -> tuple[Graph, dict[str, int], dict[int, str], int, int]:
    """Read Graph examples and returns Graph (or DiGraph)
    The example files have the following structure:
    n, m
    s, t
    <vertices> #list of size n (new line per entry)
    <edges> #list of size m (new line per entry)
    """

    with open(file_path, "r") as f:
        number_of_vertices, number_of_edges = map(int, f.readline().split())
        source, target = map(str, f.readline().split())

        all_vertices = [f.readline().strip() for _ in range(number_of_vertices)]

        all_edges = [edge.strip() for edge in f]

    
    
    #mapping from vertex name to vertex number and vice versa
    index_of_vertex = {}
    vertex_of_index = {}

    #check if graph is directed
    if ">" in all_edges[0]:
        G = DiGraph() 
    else:
        G = Graph()
    
    #Add vertices to graph
    for vertex_number, vertex_name in enumerate(all_vertices):
        G.add_vertex()

        index_of_vertex[vertex_name] = vertex_number
        vertex_of_index[vertex_number] = vertex_name
    

    
    #Add edges
    for edge in all_edges:
        vertex_from, _, vertex_to = edge.split()

        G.add_edge(u=index_of_vertex[vertex_from], 
                    v=index_of_vertex[vertex_to])
    
    return G, index_of_vertex, vertex_of_index, source, target


def main():
    grap_files = ["G-ex.txt",
                "grid-5-0.txt",
                "increase-n8-1.txt",
                "P3.txt",
                "rusty-1-17.txt",
                "ski-illustration.txt"
                ]

    for file_name in grap_files:
    #for file_name in [grap_files[-1]]:
        print(file_name)
        path = f"../data/Graphs/{file_name}"

        #G = ReadGraphExample(path)
        G, v_to_i, i_to_v, s, t = ReadGraphExample(path)

        print(len(G.G))
        print(G)
        #print(f"vertex to name: {v_to_i}")
        #print(f"name to vertex: {i_to_v}")
        #print(f"source: {s}, target: {t}")
        print()
    return


if __name__ == "__main__":
    main()