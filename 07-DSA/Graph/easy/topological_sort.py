"""
Topological sort is the linear ordering of the vertices (nodes) in directed acyclic graph(DAG) such that
every directed edge (u,v), vertex u comes before the vertex v. 

In other words it arranges nodes in such a way that if there is directed edge from node A to node B, 
then node A comes before node B.
"""
from collections import deque
class TopologicalSort:

    def solution(self, vertices: int , edges: list[list[int]])-> list[int]:
        """
        """

        # Ajdanceny list
        graph = [[] for _ in range(vertices+1)]
        for u, v in edges:
            graph[u].append(v)

        print(graph)
        # Calculate the indegree of each node 
        indegree = [0] * (vertices+1)
        for i in range(1, len(indegree)):
            for nbr in graph[i]:
                indegree[nbr] += 1

        # Add the node with indegree 0 to the queue. These are freed nodes
        q = deque()
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        # Free other nodes and add to answer
        ans = []
        while len(q) > 0:
            rem = q.popleft()
            ans.append(rem)

            # Free its neighbour
            for nbr in graph[rem]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    q.append(nbr)
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
