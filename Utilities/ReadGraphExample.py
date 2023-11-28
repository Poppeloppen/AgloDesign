import sys
sys.path.append("../")
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

        #mapping from vertex name to vertex number and vice versa
        self.index_of_vertex = dict()
        self.vertex_of_index = dict()

        self._read_graph_data(file_path)

        self.G = self._create_graph_object()
        self.add_vertices()
        
        #TODO: make sure to call this function explicitly in the files where GraphCreator is used
        #self.add_edges()


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
    

    def add_vertices(self):
        """Add all vertices to graph"""
        for vertex_idx, vertex_name in enumerate(self.all_vertices):
            self.G.add_vertex()
            self.index_of_vertex[vertex_name] = vertex_idx
            self.vertex_of_index[vertex_idx] = vertex_name

        return


    def add_edges(self) -> None:
        """Add all edges to the graph"""
        
        for edge in self.all_edges:
            vertex_from, _, vertex_to = edge.split()             
            vertex_from_idx = self.index_of_vertex[vertex_from]
            vertex_to_idx = self.index_of_vertex[vertex_to]

            self.G.add_edge(u=vertex_from_idx, 
                            v=vertex_to_idx)
                        
        return




class NoneGraphCreator(GraphCreator):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        
        #mapping from vertex name to vertex number and vice versa
        #self.index_of_vertex = dict()
        #self.vertex_of_index = dict()

        self.add_vertices()
        self.add_edges()

        self.source_idx = self.index_of_vertex[self.source]
        self.target_idx = self.index_of_vertex[self.target]


    def _valid_vertex(self, vertex_name: str) -> bool:
        """Returns true if a vertex is either non-red or is the source or target vertex."""
        if vertex_name in {self.source, self.target} or (self.is_vertex_red[vertex_name] == 0):
            return True
        
        return False


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

            #Check both vertices
            if self._valid_vertex(vertex_from) and self._valid_vertex(vertex_to):

                vertex_from_idx = self.index_of_vertex[vertex_from]
                vertex_to_idx = self.index_of_vertex[vertex_to]

                self.G.add_edge(u=vertex_from_idx, 
                                v=vertex_to_idx)
                        
        return

    

class AlternateGraphCreator(GraphCreator):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        #self.index_of_vertex = dict()
        #self.vertex_of_index = dict()

        self.add_vertices()
        self.add_edges()

        self.source_idx = self.index_of_vertex[self.source]
        self.target_idx = self.index_of_vertex[self.target]


    def _different_color(self, vertex1: str, vertex2: str) -> bool:
        """True if vertex1 and vertex2 have different colors?"""
        return not (self.is_vertex_red[vertex1] == self.is_vertex_red[vertex2])

    #TODO: I'm pretty sure this is redundant since the exact same method is part of parent
    def add_vertices(self):
        """Add all vertices to graph"""
        for vertex_idx, vertex_name in enumerate(self.all_vertices):
            self.G.add_vertex()
            
            self.index_of_vertex[vertex_name] = vertex_idx
            self.vertex_of_index[vertex_idx] = vertex_name

        return

    def add_edges(self) -> None:
        """Only add edges between vertices of different color"""
        
        for edge in self.all_edges:
            vertex_from, _, vertex_to = edge.split()         

            #Check both vertices
            if self._different_color(vertex_from, vertex_to):
                vertex_from_idx = self.index_of_vertex[vertex_from]
                vertex_to_idx = self.index_of_vertex[vertex_to]

                self.G.add_edge(u=vertex_from_idx, 
                                v=vertex_to_idx)
                        
        return



class FewGraphCreator(GraphCreator):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.add_edges()#vertex_to_connect_to_source = red_vertex)

        self.source_idx = self.index_of_vertex[self.source]
        self.target_idx = self.index_of_vertex[self.target]

    def add_edges(self) -> None:
        """Add large weight to edges going to red vertices"""
        
        for edge in self.all_edges:
            vertex_from, _, vertex_to = edge.split()         

            vertex_from_idx = self.index_of_vertex[vertex_from]
            vertex_to_idx = self.index_of_vertex[vertex_to]

            #Penalize edges going to red vertices
            if self.is_vertex_red[vertex_to]:
                self.G.add_edge(u=vertex_from_idx, v=vertex_to_idx, w=10**7)
            
            else:
                self.G.add_edge(u=vertex_from_idx, v=vertex_to_idx, w=1)

                        
        return





class SomeGraphCreator(GraphCreator):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.create_additional_vertices()
        self.add_edges()

        self.source_idx = self.index_of_vertex[self.source]
        self.target_idx = self.index_of_vertex[self.target]
        
    
    def create_additional_vertices(self) -> None:
        """Double the number of vertices + 2 to facilitate splitting each vertex
        and adding source + sink vertices.
        """
        for _ in range(self.number_of_vertices + 2):
            self.G.add_vertex()
        
        return


    def add_edges(self):#, vertex_to_connect_to_source: int) -> None:
        
        #from v_1_in -> v_1_out and v_1_out->(v_n_in)
        for edge in self.all_edges:
            vertex_from, _, vertex_to = edge.split()         

            vertex_from_idx = self.index_of_vertex[vertex_from]
            vertex_to_idx = self.index_of_vertex[vertex_to]

            print(f"{edge}: ({vertex_from_idx}, {vertex_to_idx})")

            #v_1_in -> v_1_out
            self.G.add_edge(u=vertex_from_idx, v=vertex_from_idx+self.number_of_vertices)

            
            

        #from  new_source -> some_red_vertex (capacity: 2)


        #from (old_target, old_source) -> new_target (capacity: 1 (each))

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

        #G = GraphCreator(path)

        #G_none = NoneGraphCreator(path)

        #G_alt = AlternateGraphCreator(path)
        
        #G_few = FewGraphCreator(path)
        #print(G_few.G)

        G_some = SomeGraphCreator(path)
        
        #TODO: I need to iterate over this list and run the FordFulkerson for each value
        #indices_of_reds = [index for index, value in enumerate(G_some.red_vertices) if value == 1]

        #print(indices_of_reds)
        
        print(G_some.G)

        print()
    return


if __name__ == "__main__":
    main()