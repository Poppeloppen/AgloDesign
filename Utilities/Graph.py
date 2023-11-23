from typing import Iterator

class Graph:
    def __init__(self, G: list[dict[int, int]] = []) -> None:
        self.G = G
        self.number_of_vertices = 0
        self.number_of_edges = 0

    def add_vertex(self) -> None:
        self.G.append(dict())
        self.number_of_vertices += 1
        return

    def add_edge(self, u: int, v: int, w: int = 1) -> None:
        """Add an edge between u and v with capacity w, 
        """
        assert(max(u,v) < len(self.G)), f"u ({u}) and v ({v}) should be smaller than the size of G ({len(self.G)}) --> you should add additional vertices to G"
        self.G[u][v] = w
        self.G[v][u] = w
        self.number_of_edges += 2
        return

    def size(self) -> int:
        return self.number_of_vertices

    def __str__(self) -> str:
        str = ""
        for node, adj in enumerate(self.G):
            str += f"{node}: {adj}\n"
        return str
    
    def __iter__(self) -> Iterator[dict[str, int]]:
        return iter(self.G)

    def __getitem__(self, item: int) -> dict[str, int]:
        return self.G[item]



class DiGraph(Graph):
    def __init__(self, G: list[dict[str, int]] = []):
        super().__init__(G)

    def add_edge(self, u: int, v: int, w: int = 1) -> None:
        self.G[u][v] = w
        self.number_of_edges += 1
        return
        


def main():
    n = 10

    G = Graph()
    dG = DiGraph()

    G.add_vertex()
    dG.add_vertex()
    for i in range(1, 10):    
        G.add_vertex()
        G.add_edge(i-1, i)
    
        dG.add_vertex()
        dG.add_edge(i-1, i)
    
    
    

    print(G)
    print(G.number_of_vertices)
    print(G.number_of_edges)
    
    print(dG)
    print(dG.number_of_vertices)
    print(dG.number_of_edges)
    print()
    



if __name__ == "__main__":
    main()
