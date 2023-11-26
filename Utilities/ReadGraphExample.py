from Utilities.Graph import Graph, DiGraph


class GraphCreator():
    def __init__(self, file_path: str) -> None:
        self.number_of_vertices = None
        self.number_of_edges = None
        self.source = None
        self.target = None
        self.all_vertices = None
        self.all_edges = None
        self.red_vertices = None

        self._read_graph_data(file_path)

        self.G = self._create_graph_object()


    def _read_graph_data(self, file_path: str) -> None:
        
        with open(file_path, "r") as f:
            self.number_of_vertices, self.number_of_edges, self.cardinality = map(int, f.readline().split())
            self.source, self.target = map(str, f.readline().split())

            all_vertix_data = [f.readline().strip().split() for _ in range(self.number_of_vertices)]
            self.all_vertices = [v[0] for v in all_vertix_data]
            self.red_vertices = [0 if v[-1] != '*' else 1 for v in all_vertix_data]
            
            #Dictionary with vertex name as key and value of 1 if the vertex is red, otherwise 0
            self.is_vertex_red = {v[0]:(0 if v[-1] != '*' else 1) for v in all_vertix_data}

            self.all_edges = [edge.strip() for edge in f]
        
        return


    def _create_graph_object(self) -> Graph:
        #check if graph is directed
        if ">" in self.all_edges[0]:
            G = DiGraph() 
        else:
            G = Graph()
        
        return G
    



class NoneGraphCreator(GraphCreator):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        
        #mapping from vertex name to vertex number and vice versa
        self.index_of_vertex = dict()
        self.vertex_of_index = dict()

        self.add_vertices()
        self.add_edges()

        self.source_idx = self.index_of_vertex[self.source]
        self.target_idx = self.index_of_vertex[self.target]


    def _valid_vertex(self, vertex_name: str) -> bool:
        """Returns true if a vertex is either black or is the source or target vertex."""
        if vertex_name in {self.source, self.target} or (self.is_vertex_red[vertex_name] == 0):
            return True
        
        return False


    #TODO: Ensure that source and target vertex is always added
    def add_vertices(self):
        """Add all non-red vertices to graph"""
        
        vertex_idx = 0
        for vertex_name in self.all_vertices:
            if self._valid_vertex(vertex_name):
                self.G.add_vertex()
                
                self.index_of_vertex[vertex_name] = vertex_idx
                self.vertex_of_index[vertex_idx] = vertex_name
                vertex_idx += 1

        return
    

    def add_edges(self):
        """Create edges between non-red vertices"""
        for edge in self.all_edges:
            vertex_from, _, vertex_to = edge.split()         

            #Ensure that neither vertex is red
            if self._valid_vertex(vertex_from) and self._valid_vertex(vertex_to):

                vertex_from_idx = self.index_of_vertex[vertex_from]
                vertex_to_idx = self.index_of_vertex[vertex_to]

                self.G.add_edge(u=vertex_from_idx, 
                                v=vertex_to_idx)
                        
        return

    



def main():
    grap_files = ["G-ex.txt",
                #"grid-5-0.txt",
                #"increase-n8-1.txt",
                #"P3.txt",
                #"rusty-1-17.txt",
                #"ski-illustration.txt",
                #"wall-n-10000.txt"
                ]

    for file_name in grap_files:
        print(file_name)
        path = f"../data/Graphs/{file_name}"

        #G = GraphCreator(path)
        #print(G.all_vertices)
        #print(G.red_vertices)

        G_none = NoneGraphCreator(path)
        G_none.add_vertices()
        print(G_none.G)


        G_none.add_edges()
        print(G_none.G)
        print(G_none.vertex_of_index)
        #print(G_none.all_vertices)
        #print(G_none.red_vertices)
        #print(G_none.all_edges)
        #print(type(G_none))
        #print(type(G_none.G))
        #G, v_to_i, i_to_v, s, t = ReadGraphExample(path)
        #print(len(G.G))
        print()
    return


if __name__ == "__main__":
    main()