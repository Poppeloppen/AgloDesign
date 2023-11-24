from typing import Iterator

class Graph:
    def __init__(self, G: list[dict[int, int]] = None) -> None:
        self.G = G if G is not None else []
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
    def __init__(self, G: list[dict[str, int]] = None):
        super().__init__(G)
        #self.G = G

    def add_edge(self, u: int, v: int, w: int = 1) -> None:
        self.G[u][v] = w
        self.number_of_edges += 1
        return
        


def main():
    for i in range(10):
        G = Graph()

        for j in range(2):
            G.add_vertex()
    
        print(G.G)
        
    return



if __name__ == "__main__":
    main()
