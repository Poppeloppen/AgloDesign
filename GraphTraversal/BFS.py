from typing import Optional

import sys
sys.path.append("../")
from Utilities.Graph import Graph, DiGraph


class BFS:
    """A BFS algorithm that starts at a given source vertex and computes the path to all
    other vertices and the distances to these. In case a target vertex is specified the 
    algorithm will stop as soon as the target vertex is encountered.
    """
    def __init__(self, G: Graph, source: int, target: Optional[int] = None) -> None:
        self._discovered = [False] * G.number_of_vertices   #is there a path from s to i?
        self._dist_to = [float("inf")] * G.number_of_vertices   #what is the dist from s to i?
        self._edge_to = [None] * G.number_of_vertices   #what vertex comes before i in shortest path? 
        self.number_of_vertices = G.number_of_vertices

        self._bfs(G, source, target)


    def _bfs(self, G: Graph, source: int, target: Optional[int]) -> None:
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"
        #Always start BFS from the provided source
        self._discovered[source] = True
        self._dist_to[source] = 0
        queue = [source]

        while queue:
            current_node = queue.pop(0) #pop first element

            #Go through all the (not already visited) neighbours of the current node one by one (and store relevant info)
            for neighbour in G[current_node].keys():
                if not self._discovered[neighbour]:
                    self._discovered[neighbour] = True
                    self._dist_to[neighbour] = self._dist_to[current_node] + 1
                    self._edge_to[neighbour] = current_node
                    queue.append(neighbour)

                    if neighbour == target: #If target is specified, stop as soon as found
                        return
                    
        return    


    def has_path_to(self, target: int) -> bool: 
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"
        return self._discovered[target]


    def path_to(self, target: int) -> list:
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"

        path = []

        x = target
        while self._edge_to[x] != 0:
            path.insert(0, x) #insert instead of append in order to mimic stack
            x = self._edge_to[x]

        return path
    
    
    def dist_to(self, target: int) -> int:
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"

        return self._dist_to[target]
   


def main():
    n = 100000

    G = DiGraph()
    #dG = DiGraph()

    G.add_vertex()
    #dG.add_vertex()
    for i in range(1, n):    
        G.add_vertex()
        G.add_edge(i-1, i)
    
        #dG.add_vertex()
        #dG.add_edge(i-1, i)
    

    bfs = BFS(G, source=10, target=0)
    print(bfs._discovered[:50])
    
    return


if __name__ == "__main__":
    main()
