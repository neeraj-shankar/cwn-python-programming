class DFSTraversal:

    def solution(self, n: int, edges: list[tuple]):

        # Construct the adjancency list 
        graph = [ [] for _ in range(n)]

        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
        
        # Create visited array to track the unvisited and visisted vertex
        vis = [False for _ in range(n)]

        for i in range(n):

            if vis[i] == False:
                self.dfs(graph, i, vis)
    
    def dfs(self, graph:list[list[int]], src: int, vis: list[bool]):

        vis[src] = True
        print(src)
        nbrs = graph[src]

        for nbr in nbrs:
            if vis[nbr] == False:
                self.dfs(graph, nbr, vis)





if __name__ == "__main__":

    dt = DFSTraversal()

    # Test Case 1: Tree structure
    n = 7
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    print(f"Answer after traveral: {dt.solution(n, edges)}")

    # Test case 2: Disconnected Graphs
    n = 6
    edges = [(0, 1), (1, 2), (3, 4), (4, 5)]
    print(f"BFS Traversaal of disconnected graph: ", dt.solution(n, edges))
