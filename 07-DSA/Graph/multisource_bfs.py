"""
There are N number of nodes and multisources {s1, s2, s3}

Find the length of shortest path for given destination to any one of the sources.
"""
from collections import deque
class ShortestPathToDestination:

    def solve(self, nodes: int, edges: list[list[int]], sources: int, destination: int)-> int:

        # create adjancency list 
        graph = [list() for _ in range (nodes)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print(graph)

        # create visited array to track node visit status
        vis = [False] * nodes
        print(vis)

        # Traverse and put all the sources to the queue
        q = deque()
        for src in sources:
            q.append((src, 0))
            vis[src] = True
        print(q)

        # while queue does not become empty or destination is found do this:
        # 1. get the node from left of the queue
        # 2. Extract node and its distance from source
        # if the node is destination return the distance
        # else get all the neighbours to of the extracted node and add them to queue by increasing distance by 1
        while (len(q) > 0):

            rem = q.popleft()

            # Extract the details 
            node = rem[0]
            dist = rem[1]

            if node == destination:
                print(f"Shorted Path to destination {destination} is {dist}")
                return 
            
            # get the neigbours and add to queue
            for nbr in graph[node]:

                if vis[nbr] == False:
                    q.append((nbr, dist+1))
                    vis[nbr] = True

if __name__ == "__main__":

    sptd = ShortestPathToDestination()

    # Test Case 1
    nodes = 7

    edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4],
        [0, 5],
        [0, 6]
    ]

    sources = [2, 4, 6]
    destination = 1

    
    #####################################################################################
    # Test Case 2:
    nodes = 14

    edges = [
    [11, 1],
    [11, 6],
    [11, 5],

    [5, 2],
    [5, 4],

    [2, 3],

    [3, 12],
    [3, 9],

    [4, 8],

    [8, 7],

    [7, 10],

    [10, 13],

    [9, 13]
]

    sources = [11, 7, 2]
    destination = 9

    sptd.solve(nodes, edges, sources, destination)
    #####################################################################################