"""

"""

import heapq

class Pair:
    def __init__(self, vt: int, wt:int):
        self.vt = vt
        self.wt = wt 

    def __lt__(self, other):
        return self.wt < other.wt # comparator logic


class DjikstraAlgorithm:

    def solution(self, vertices: int, edges: list[list[int]]):
        
        """
        1. Contruct the adjancey list from vertices and edges
        2. Create a visited array to track unvisited vertices
        3. Create a pair class (sorting to be done based on minimum weight), 
           add the first node in min heap
        4. Now while min heap is not empty, extract the top pair, do the following:
            a. Verify if the extracted node is already visited, if so continue.
            b. if no, mark it as visited, add the aggregated distance (weight) to distance array.
            c. Traverse through its neighbours, add all its unvisited neighbour to heap.
        """
        # Construct the adjances list from given vertces and edges
        graph = [[] for _ in range(vertices+1)]

        for edge in edges:
            u, v, wt = edge
            graph[u].append(Pair(v, wt))

        for ls in graph:
            for pr in ls:
                print(f"Vertex: {pr.vt} and Edge: {pr.wt}")

        # Create the distance array to store distance of each vertex from source
        dist = [float('-inf') for _ in range(vertices+1)]

        # Add the first source to the priority queue
        min_heap = []
        heapq.heappush(min_heap, Pair(1, 0)) 
        while len(min_heap) > 0:

            rem = heapq.heappop(min_heap)

            vertex = rem.vt
            wsf = rem.wt

            if dist[vertex] != float('-inf'): 
                continue
            else:
                dist[vertex] = wsf 
                for nbr in graph[vertex]:
                    if dist[nbr.vt] == float('-inf'): # look for unvisited neighbour
                        nbr.wt = nbr.wt + wsf # Aggregated weight from source
                        heapq.heappush(min_heap, nbr)
        return dist
if __name__ == "__main__":

    da = DjikstraAlgorithm()

    edges = [(1, 2, 5), (1, 3, 5), (2, 4, 1), (2, 5, 5), (3, 5, 3)]
    vertices = 5
    print(f"Distance of all destination from source: {da.solution(vertices, edges)}")