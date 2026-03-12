"""
Flipkart has A local distribution centers located across a large metropolitan city. 
Each distribution center needs to be interconnected through roads to facilitate efficient movement of goods.

The cost of constructing a road between any two distribution centers is represented by the weight of 
the edge connecting them.

Given a graph with A nodes representing the distribution centers and C weighted edges representing the 
possible roads between them, your task is to find the minimum total cost of constructing roads 
such that every distribution center can be reached from the first distribution center.

Cost Calculation:
The cost of constructing the roads is the sum of the weights of the edges selected for the construction.

NOTE: Return the answer modulo 10^9+7 as the answer can be large.
"""

import heapq

class Pair:

    def __init__(self, cost :int, vt: int):
        self.cost = cost 
        self.vt = vt 

    def __lt__(self, other):

        return self.cost < other.cost
    
class ConstructionCost():

    def solution_prims(self, A: int, B: list[list[int]]) -> int:
        """
        
        """
        # Size of the matrix --> totals rows
        n = len(B)
        # Create visited array of size A to track visted nodes
        visited = [False for _ in range(A+1)]

        # Create the adjacency list from given matrix
        graph = [[] for _ in range(A+1)]
        for i in range(0, n):
            u = B[i][0]
            v = B[i][1]
            wt = B[i][2]
            graph[u].append(Pair(wt, v))

        print(graph)

        # Create Priority Queue --> minheap
        pq = []
        heapq.heappush(pq, Pair(0, 1))
        ans = 0
        while(len(pq) > 0):

            # Remove
            rem = heapq.heappop(pq)
            vt = rem.vt
            cost = rem.cost
            

if __name__ == "__main__":

    cc = ConstructionCost()

    #Test case 1:
    A = 3
    B = [   [1, 2, 14], [2, 3, 7], [3, 1, 2]   ]
    print(f"Minimum cost to build: {cc.solution_prims(A, B)}")
    # pq = []
    # heapq.heappush(pq, Pair(10, 1))
    # heapq.heappush(pq, Pair(5, 2))
    # heapq.heappush(pq, Pair(20, 3))

    # while pq:
    #     p = heapq.heappop(pq)
    #     print(p.cost, p.vt)