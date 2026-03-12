"""
You are given an integer array A of length N, where A[i] represents the cost of stepping on the 
i-th stair of a staircase.

Once you pay the cost of a stair, you can either:
1. climb one step, or
2. climb two steps.

You are allowed to start from either the 0th index stair or the 1st index stair.

🔁 Additional Constraint (Twist)
You are also given an integer B, representing a specific stair that must be visited while climbing.
You cannot skip the B-th stair.

Your task is to find the minimum cost required to reach the top of the staircase, 
while ensuring that the B-th stair is stepped on.

📝 Note
Reaching the top of the staircase means reaching the N-th stair (i.e., beyond the last index).

"""

class MinimumCostWithNonSkip:

    def solution(self, A, B):
        """
        1. Build a min cost array
        2. Handle the exceptional case for B.
        3. If B is the last index, return value stored at Bth index otherwise minimum of last and second last
        """
        n = len(A)

        cost = [0 for _ in range(n)]
        cost[0] = A[0]
        cost[1] = A[1]

        for i in range(2, n):

            cost[i] = min(cost[i-1], cost[i-2]) + A[i]

        print(f"Min cost Array before B-interfere: {cost}")
        # Check if B is the last index
        if B == n-1:
            return cost[B]
        
        # Handle when B is somewhere in the middle
        # Cost to reach B+1th index
        cost[B+1] = cost[B] + A[B+1]

        for j in range(B+2, n):

            cost[j] = min(cost[j-2], cost[j-1]) + A[j]

        print(f"Min cost Array after B-interferes: {cost}")

        # Return the min of n-1 vs n-2th index
        return min(cost[n-1], cost[n-2])
    
    def solution_fixed(self, A, B):
        """
        1. Build a min cost array
        2. Handle the exceptional case for B.
        3. If B is the last index, return value stored at Bth index otherwise minimum of last and second last
        """
        n = len(A)

        cost = [0 for _ in range(n)]
        cost[0] = A[0]
        cost[1] = A[1]

        for i in range(2, n):

            cost[i] = min(cost[i-1], cost[i-2]) + A[i]

        print(f"Min cost Array before B-interfere: {cost}")
        # Check if B is the last index
        if B == n-1:
            return cost[B]
        
        # Handle when B is somewhere in the middle
        # Cost to reach B+1th index
        cost2 = [0 for _ in range(n)]
        cost2[B] = cost[B]

        cost2[B+1] = cost2[B] + A[B+1]

        for j in range(B+2, n):

            cost2[j] = min(cost2[j-2], cost2[j-1]) + A[j]

        print(f"Min cost Array after B-interferes: {cost}")

        # Return the min of n-1 vs n-2th index
        return min(cost2[n-1], cost2[n-2])


if __name__ == "__main__":

    mcws = MinimumCostWithNonSkip()

    # Test Case 1:
    A = [6, 2, 2, 1, 5]
    B = 2
    print(f"Minimum cost to cross: {mcws.solution(A, B)}")
    print(f"Minimum cost to cross opti: {mcws.solution(A, B)}")


    # Test Case 2: Bth is last stair
    A = [1, 100, 1, 1, 1, 100, 1]
    B = 6
    print(f"Minimum cost to cross: {mcws.solution(A, B)}")
    print(f"Minimum cost to cross opti: {mcws.solution(A, B)}")


    # Test Case 3: Increasing cost
    A = [1, 2, 3, 4, 5]
    B = 2
    print(f"Minimum cost to cross: {mcws.solution(A, B)}") # 9 
    print(f"Minimum cost to cross opti: {mcws.solution_fixed(A, B)}")

    A = [1, 1, 100, 1]
    B = 1
    print(f"Minimum cost to cross: {mcws.solution(A, B)}") # 9 







