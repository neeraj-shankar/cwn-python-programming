"""
Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.

You have to find an integer array D of size A such that:

D[i]: Shortest distance from the C node to node i.
If node i is not reachable from C then -1.
Note:

There are no self-loops in the graph.
There are no multiple edges between two pairs of vertices.
The graph may or may not be connected.
Nodes are numbered from 0 to A-1.
Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.
"""

import heapq

class Pair:

    def __init__(self, vt, wt):
        self.vt = vt
        self.wt = wt

    def __lt__(self, other):

        return self.wt < other.wt # Helps in natural sorting based on minimum weight
    
class Djikstra:

    def solution(self, A: int, B: list[list[int]], C:int)-> list[int]:
        """
        1. Construct the adjancency list 
        2. Create distance to store minimum distance from source
        3. Add the source to the minheap sorted by minimum weight
        """
        graph = [[] for _ in range(A+1)]

        for u, v, wt in B:
            graph[u].append(Pair(v, wt))
            graph[v].append(Pair(u, wt))

        # Dist array to store distance from source
        dist = [float('-inf') for _ in range(A)]

        min_heap = []
        heapq.heappush(min_heap, Pair(C, 0))

        while len(min_heap) > 0:

            # Extract the node
            rem = heapq.heappop(min_heap)

            node = rem.vt
            wsf = rem.wt

            if dist[node] != float('-inf'):
                continue
            else:
                dist[node] = wsf
                for nbr in graph[node]:
                    nvt = nbr.vt
                    nwt = nbr.wt

                    if dist[nvt] == float('-inf'):
                        nbr.wt = nbr.wt + wsf
                        heapq.heappush(min_heap, nbr)

        return dist


if __name__ == "__main__":

    djikstra = Djikstra()

    # Test Case 1:
    A = 6
    B = [[0, 4, 9],[3, 4, 6],[1, 2, 1],[2, 5, 1],[2, 4, 5],[0, 3, 7],[0, 1, 1],[4, 5, 7],[0, 5, 1]]
    C = 4

    print(f"Minimum distance array: {djikstra.solution(A, B, C)}")

    # Test Case 2:
    A = 5
    B = [   [0, 3, 4], [2, 3, 3], [0, 1, 9], [3, 4, 10], [1, 3, 8]] 
    C = 4
    print(f"Minimum distance array: {djikstra.solution(A, B, C)}")

    # Test Case 3:
    A = 7
    B = [[2,4,10],[3,4,1],[3,6,1],[1,2,4],[4,5,6]]
    C = 2
    print(f"Minimum distance array: {djikstra.solution(A, B, C)}")


