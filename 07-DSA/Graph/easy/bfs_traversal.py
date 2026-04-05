""" """

from collections import deque


class BFSTraversal:

    def solution(self, n: int, edges: list[tuple]) -> list:

        # Create a adjancency list from given edges
        graph = [[] for _ in range(n)]
        for edge in edges:

            u = edge[0]
            v = edge[1]
            graph[u].append(v)

        print(graph)

        # Create a visited array of size n
        vis = [False for _ in range(n)]
        ans = []
        # Do the traversal for node that is not visited yet
        for i in range(0, n):
            if vis[i] == False:
                self.bfs(graph, i, vis, ans)

        return ans

    def bfs(
        self, graph: list[list[int]], src: int, vis: list[int], ans: list[int]
    ) -> None:

        # 1. Create a queue
        q = deque()

        # 2. Add source node and mark it as true visited arr
        q.append(src)
        vis[src] = True

        # For the rest of part, remove, perform, and add the neighbour
        while len(q) > 0:

            # Remove the node
            rem = q.popleft()

            # Add to the answer
            ans.append(rem)

            # Extract and add the neighbours
            for nbr in graph[rem]:
                if vis[nbr] == False:
                    q.append(nbr)
                    vis[nbr] = True


if __name__ == "__main__":

    bt = BFSTraversal()

    # Test Case 1: Tree structure
    n = 7
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    print(f"Answer after traveral: {bt.solution(n, edges)}")

    # Test case 2: Disconnected Graphs
    n = 6
    edges = [(0, 1), (1, 2), (3, 4), (4, 5)]
    print(f"BFS Traversaal of disconnected graph: ", bt.solution(n, edges))
