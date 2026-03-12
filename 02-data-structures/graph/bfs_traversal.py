"""
BFS --> Breadth First Search
-------------------------------------------------
A graph traversal algorithm used to explore or nagivate a tree or graph. Starts with source node
and explore all its neighbour at current depth.
"""

from collections import deque


class BreadthFirstSearch:

    def solution(self, vertex: int, edges: list[tuple[int]]):
        # Create adjacency array from given vertexes and edges
        graph = [[] for _ in range(vertex)]

        for u, v in edges:
            graph[u].append(v)

        # visited array to mark whether the node is explored
        vis = [False for _ in range(vertex)]

        ans = []
        for i in range(len(vis)):

            if vis[i] == False:
                self.bfs(graph, i, vis, ans)

        return ans

    def bfs(self, graph: list[list[int]], src: int, vis: list[int], ans: list) -> None:
        """
        Steps
        -----------------------------------------
        1. Take a queue.
        2. Add the source node to the queue. Mark it as visited.
        3. while queue size is greater than 0 (that is queue is not empty):
            a. Remove from front.
            b. process the removed node
            c. add its unvisited neighbours and mark them as visisted.
        """

        q = deque()

        # Add the source node and mark it as visited
        q.append(src)
        vis[src] = True

        while q.__len__() > 0:

            # Remove
            rem = q.popleft()

            # Process
            ans.append(rem)

            # Add the unxplored neighbours
            for nei in graph[rem]:
                # print(f"Current Neighbour of {rem} is : {nei}")
                if vis[nei] == False:
                    q.append(nei)
                    vis[nei] = True


if __name__ == "__main__":
    obj = BreadthFirstSearch()

    # Test case 1:
    v = 4
    edges = [(0, 1), (1, 2), (2, 3)]
    print(f"All nodes: {obj.solution(v, edges)}")

    # Test case 2: Tree Structure (Classic BFS)
    v = 7
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    print(f"All nodes: {obj.solution(v, edges)}")

    # Test Case 3: Disconnected Graph (Very Important)
    v = 6
    edges = [(0, 1), (1, 2), (3, 4)]

    print(f"All nodes: {obj.solution(v, edges)}") # [0, 1, 2, 3, 4, 5]

    # Test Case 4: Graph with Cycle
    v = 4
    edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
    print(f"All nodes: {obj.solution(v, edges)}") #[0, 1, 2, 3]
   
    # Test Case 5: Single Node
    v = 1
    edges = []
    print(f"All nodes: {obj.solution(v, edges)}") # [0]

    # Test Case 6: Completely Isolated Nodes
    v = 5
    edges = []
    print(f"All nodes: {obj.solution(v, edges)}") # [0, 1, 2, 3, 4]

    # Test Case 7: Multiple Paths to Same Node (Bug Catcher)
    v = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    print(f"All nodes: {obj.solution(v, edges)}") # [0, 1, 2, 3]
