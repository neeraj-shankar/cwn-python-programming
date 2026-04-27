"""
Given a weighted undirected graph having A nodes, a source node C and destination node D.

Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.

You are expected to do it in Time Complexity of O(A + M).

Note:
1. There are no self-loops in the graph.
2. No multiple edges between two pair of vertices.
3. The graph may or may not be connected.
4. Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.

Problem Constraints
-------------------------------------------------
1 <= A <= 105
0 <= B[i][0], B[i][1] < A
1 <= B[i][2] <= 2
0 <= C < A
0 <= D < A

"""

from collections import deque
class AnotherBFS:

    def solution(self, A: int, B: list[list[int]], C: int, D: int):


        # Create ajancency list for undirected graph
        n = len(B)
        graph = [[] for _ in range(A + n)]
        dummy = A
        for u, v, wt in B:
            print("current relation", u, v, wt)
            if wt == 1:
                graph[u].append(v)
                graph[v].append(u)
            else:
                graph[u].append(dummy)
                graph[dummy].append(u)

                graph[dummy].append(v)
                graph[v].append(dummy)

                dummy += 1
        print(graph) 

        dist = [-1] * dummy

        qeue = deque()
        qeue.append(C)
        dist[C] = 0

        while len(qeue) > 0:

            rem = qeue.popleft()

            for nbr in graph[rem]:
                if dist[nbr] == -1:
                    dist[nbr] = dist[rem] + 1
                    qeue.append(nbr)
        print(dist)
        return dist[D]


        


if __name__ == "__main__":

    ab = AnotherBFS()

    # Test case 1:
    A = 6
    B = [[2, 5, 1], [1, 3, 1], [0, 5, 2], [0, 2, 2], [1, 4, 1], [0, 1, 1]]
    C = 3
    D = 2
    print(f"Minumum Distance: {ab.solution(A, B, C, D)}")
