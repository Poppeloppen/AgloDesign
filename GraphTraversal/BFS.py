import sys
sys.path.append("../")
from Utilities.Graph import Graph
from DynamicProgramming.Fibonacci import fibonacci_iterative



class BFS:
    def __init__(self, G: Graph, source: int) -> None:
        self._discovered = [False] * G.number_of_vertices   #is there a path from s to i?
        self._dist_to = [float("inf")] * G.number_of_vertices   #what is the dist from s to i?
        self._edge_to = [None] * G.number_of_vertices   #what vertex comes before i in shortest path? 
        self.number_of_vertices = G.number_of_vertices
        
        self._bfs(G, source)


    def _bfs(self, G: Graph, source: int):
        self._discovered[source] = True
        self._dist_to[source] = 0
        queue = [source]

        while queue:
            current_node = queue.pop(0)

            print(f"node {current_node}'s neighbors: {G[current_node]}")
            for neighbour in G[current_node].keys():
                if not self._discovered[neighbour]:
                    self._discovered[neighbour] = True
                    self._dist_to[neighbour] = self._dist_to[current_node] + 1
                    self._edge_to[neighbour] = current_node
                    queue.append(neighbour)
                    
        return    


    def has_path_to(self, target: int) -> bool: 
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"
        return self._discovered[target]


    def path_to(self, target: int) -> list:
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"

        x = target

        path = []
        while self._edge_to[x] != 0:
            path.append(x)
            x = self._edge_to[x]

        p = list(reversed(path))
        return p
    
    
    def dist_to(self, target: int) -> int:
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"

        return self._dist_to[target]

    
    


def main():
    n = 10

    G = Graph()
    #dG = DiGraph()

    G.add_vertex()
    #dG.add_vertex()
    for i in range(1, 10):    
        G.add_vertex()
        G.add_edge(i-1, i)
    
        #dG.add_vertex()
        #dG.add_edge(i-1, i)
    


    #print(G[2].keys())

    print(G)
    bfs = BFS(G, 0)
    print(bfs.has_path_to(9))
    print(bfs.dist_to(9))
    print(bfs.path_to(9))
    
    return


if __name__ == "__main__":
    main()
