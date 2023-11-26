from typing import Optional

import sys
sys.path.append("../")
from Utilities.Graph import Graph, DiGraph
from Utilities.ReadGraphExample import ReadGraphExample

class DFS:
    def __init__(self, G: Graph, source: int, target: Optional[int] = None) -> None:
        self._discovered = [False] * G.number_of_vertices
        self._dist_to = [-1] * G.number_of_vertices
        self._edge_to = [None] * G.number_of_vertices
        
        self._dfs(G, s)
        pass

    def _dfs(self, G: Graph, source: int) -> None:
        
        self._discovered[source] = True
        self._dist_to[source] = 0

        stack = [source]
        
        while stack:
            stack.pop() #pop last element
            
            for neighbour in G[current_node].keys():
                if not self._discovered[neighbour]:
                    self._discovered[neighbour] = True
                    self._dist_to[neighbour] = self._dist_to[current_node] + 1
                    self._edge_to[neighbour] = current_node
                    stack.append(neighbour)

                    if neighbour == target: #If target is specified, stop as soon as found
                        return


        return
    

    def has_path_to(self, t):
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"
        return 
    
    def dist_to(self, t):
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"
        return
    
    def path_to(self, t):
        assert target < self.number_of_vertices, f"the specified target ({target}) should be smaller than size of G ({self.number_of_vertices})"
        return



def main():
    #data = ReadGraphExample("../data/Graphs/G-ex.txt")
    #print(data)
    return

if __name__ == "__main__":
    main()