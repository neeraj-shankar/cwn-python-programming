"""
You are given an undirected graph with:
A nodes and |B| edges, where the i-th edge connects nodes B[i][0] and B[i][1]

Definitions:
---------------------------------------------------------------------------------------
The strength of a connected component is defined as the number of edges in that component.

You are also given an integer C, representing the maximum number of edges you are allowed to add to the graph.
Task

Determine the maximum possible strength that any connected component in the graph can achieve after adding at most C edges.


Constraints / Notes
--------------------------------------------------------------------------------------
The graph is undirected
Edges (i, j) and (j, i) are considered identical
Duplicate edges are not allowed
Self-loops (i, i) are not allowed
"""

from collections import deque


class StrengthenIt:

    def solution(self, A: int, B: list[list[int]], C: int):

        n = len(B)
        # Build the adjancency list
        graph = [[] for _ in range(A + 1)]

        for i in range(0, n, 1):

            u = B[i][0]
            v = B[i][1]
            graph[u].append(v)
            graph[v].append(u)

        # Create a visited arr
        visited = set()

        strengths = []

        # Step 1: Find connected components and count edges
        for node in range(1, A + 1):

            if node not in visited:
                queue = deque([node])
                visited.add(node)

                nodes = 0
                edges = 0
                print(f"MY QUEUE: {queue}")
                while queue:
                    curr = queue.popleft()
                    nodes += 1

                    edges += len(graph[curr])

                    for nei in graph[curr]:

                        if nei not in visited:
                            visited.add(nei)

                            queue.append(nei)
                # Each edge counted twice in undirected graph
                strengths.append(edges // 2)

        # Step 2: Sort strengths descending
        strengths.sort(reverse=True)

        # Step 3: Greedily merge components

        while C > 0 and len(strengths) > 1:
            a = strengths.pop(0)
            b = strengths.pop(0)

            strengths.append(a + b + 1)
            strengths.sort(reverse=True)

            C -= 1

        return strengths[0] if strengths else 0


if __name__ == "__main__":

    si = StrengthenIt()

    # Test case 1:
    A = 7
    B = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]
    C = 1
    print(f"Maximum Strenght: {si.solution(A, B, C)}")
