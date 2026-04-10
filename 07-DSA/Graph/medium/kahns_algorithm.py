"""
Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Return the topological ordering of the graph and if it doesn't exist then return an empty array.

If there is a solution return the correct ordering. If there are multiple solutions print the lexographically smallest one.

Ordering (a, b, c) is said to be lexographically smaller than ordering (e, f, g) if a < e or if(a==e) then b < f and so on.

NOTE:

There are no self-loops in the graph.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""

import heapq

class TopologicalSort:

    def solution(self, vertices: int , edges: list[list[int]])-> list[int]:
        """
        1. Create adjacency list using vertices and edges
        2. Calculate the indegree of all the vertices
        3. Create a min heap and put all nodes with indegree 0 to it
        4. While heap is not empty so following:
            a. Extract the node and free its neighbour by reducing indegree count
            b. if indegree count of the neighbour is 0, add it to the heap
        """

        # Ajdanceny list
        graph = [[] for _ in range(vertices+1)]
        for u, v in edges:
            graph[u].append(v)

        # Calculate the indegree of each node 
        indegree = [0] * (vertices+1)
        for i in range(1, len(indegree)):
            for nbr in graph[i]:
                indegree[nbr] += 1

        # Add the node with indegree 0 to the queue. These are freed nodes
        min_heap = []
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                heapq.heappush(min_heap, i)

        # Free other nodes and add to answer
        ans = []
        while len(min_heap) > 0:
            rem = heapq.heappop(min_heap)
            ans.append(rem)

            # Free its neighbour
            for nbr in graph[rem]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    heapq.heappush(min_heap, nbr)
        return ans

if __name__ == "__main__":

    ts = TopologicalSort()

    # Test Case 1:
    A = 6
    B = [ [6, 3], [6, 1], [5, 1], [5, 2], [3, 4], [4, 2] ]
    print(f"Sorted nodes: {ts.solution(A, B)}")

    # Test Case 2:
    A = 3
    B = [[1, 2], [2, 3], [3, 1] ]
    print(f"Sorted Nodes: {ts.solution(A, B)}")
