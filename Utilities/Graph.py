class Graph:
    def __init__(self, G: list[dict[str, int]] = [], directed: bool = True) -> None:
        self.G = G
        self.directed = directed
        self.number_of_vertices = 0
        self.number_of_edges = 0


    def add_vertex(self) -> None:
        self.G.append(dict())
        self.number_of_vertices += 1
        return

    def add_edge(self, u: int, v: int, w: int = 1, directed: bool = True) -> None:
        """Add an edge between u and v with capacity w, 
        """
        assert(max(u,v) < len(self.G)), f"u ({u}) and v ({v}) should be smaller than the size of G ({len(self.G)}) --> you should add additional vertices to G"
        if directed:
            self.G[u][v] = w
            self.number_of_edges += 1
        else:
            self.G[u][v] = w
            self.G[v][u] = w
            self.number_of_edges += 2
        pass

    def size():
        pass

    
    def __str__(self):
        str = ""
        for node, adj in enumerate(self.G):
            str += f"{node}: {adj}\n"
        
        return str



def main():
    n = 10

    g = Graph()

    g.add_vertex()
    for i in range(1, 10):    
        g.add_vertex()
        g.add_edge(0, i)
    
    
    
    
    
    print(g)
    print(g.number_of_vertices)
    print(g.number_of_edges)
    




if __name__ == "__main__":
    main()
