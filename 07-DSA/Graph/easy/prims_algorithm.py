"""

"""

import heapq

class Pair:
    def __init__(self, vt: int, wt:int):
        self.vt = vt
        self.wt = wt 

    def __lt__(self, other):
        return self.wt < other.wt # comparator logic


class PrimsAlgorithm:

    def solution(self, vertices: int, edges: list[list[int]]):
        

        # Construct the adjances list from given vertces and edges
        graph = [[] for _ in range(vertices+1)]

        for edge in edges:
            u, v, wt = edge
            graph[u].append(Pair(v, wt))

        for ls in graph:
            for pr in ls:
                print(f"Vertex: {pr.vt} and Edge: {pr.wt}")

        # Create visited array to track the unvisited sources
        vis = [False for _ in range(vertices+1)]
        # Add the first source to the priority queue
        min_heap = []
        heapq.heappush(min_heap, Pair(1, 0)) 
        ans = 0
        while len(min_heap) > 0:

            rem = heapq.heappop(min_heap)

            vertex = rem.vt
            weight = rem.wt

            if vis[vertex] == True: 
                continue
            else:
                vis[vertex] = True
                ans += weight
                for nbr in graph[vertex]:
                    if vis[nbr.vt] == False: # look for unvisited neighbour
                        print(nbr)
                        heapq.heappush(min_heap, nbr)
        return ans
if __name__ == "__main__":

    pa = PrimsAlgorithm()

    edges = [(1, 2, 5), (1, 3, 5), (2, 4, 1), (2, 5, 5), (3, 5, 3)]
    vertices = 5
    print(f"Total cost of tree construction: {pa.solution(vertices, edges)}")