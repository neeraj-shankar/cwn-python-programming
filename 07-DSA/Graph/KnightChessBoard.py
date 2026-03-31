"""
Given any source point, (C, D) and destination point, (E, F) on a chess board of size A x B, 
we need to find whether Knight can move to the destination or not.


The above figure details the movements for a knight ( 8 possibilities ).

If yes, then what would be the minimum number of steps for the knight to move to the said point. 
If knight can not move from the source point to the destination point, then return -1.

NOTE: A knight cannot go out of the board.
"""

from collections import deque
class KnightChessBoard:

    def solution_bfs(self, A, B, C, D, E, F):
        
        # Direction array to track possible movements
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                      (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        # Visisted array to track whether a coordinate is already visited 
        visited = [[False]* (B+1) for _ in range(A+1)]

        queue = deque()
        # Add the source and distance from source to the queue
        queue.append((C, D, 0))
        visited[C][D] = True

        while len(queue)>0:
            x, y, dist = queue.popleft()

            # Base case: When the destination is reached
            if x == E and y == F:
                return dist
            
            for dx, dy in directions:
                nx = x + dx 
                ny = y + dy 

                if 1 <= nx <= A and 1 <= ny <= B and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))

        return -1
if __name__ == "__main__":

    kb = KnightChessBoard()

    A = 8
    B = 8
    C = 1
    D = 1
    E = 8
    F = 8
    print(f"Total Steps required: {kb.solution_bfs(A, B, C, D, E, F)}")

