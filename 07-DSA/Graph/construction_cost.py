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
        MOD = 10**9 + 7
        
        # Step 1: Build graph
        graph = {i: [] for i in range(1, A + 1)}
        
        for u, v, w in B:
            graph[u].append((w, v))
            graph[v].append((w, u))
        
        # Step 2: Min Heap
        min_heap = []
        heapq.heappush(min_heap, (0, 1))  # (cost, node)
        
        # Step 3: Visited array
        visited = [False] * (A + 1)
        
        total_cost = 0
        nodes_used = 0   # optional (for safety check)
        
        # Step 4: Prim's Algorithm
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            
            if visited[node]:
                continue
            
            # Mark visited
            visited[node] = True
            total_cost = (total_cost + cost) % MOD
            nodes_used += 1
            
            # Explore neighbors
            for nei_cost, neighbor in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (nei_cost, neighbor))
        
        # Optional: check if all nodes connected
        if nodes_used != A:
            return -1
        
        return total_cost
    
if __name__ == "__main__":

    cc = ConstructionCost()

    #Test case 1:
    A = 3
    B = [   [1, 2, 14], [2, 3, 7], [3, 1, 2]   ]
    print(f"Minimum cost to build: {cc.solution_prims(A, B)}")

