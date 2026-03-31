"""
In the mysterious village of Two Rivers, you find a Magical Bridge.
The bridge consists of N wooden planks, numbered from 1 to N.

You are a normal human being, so in one step you can move forward by only one plank.
However, the bridge is magical and grants you a special power:
    - If you are currently standing on plank i, you can also move forward by A[i] planks in a single step.

You are being chased by monsters and want to cross the bridge in the minimum number of steps.

Important Notes
-------------------------------------------------------------
You start at plank 1 (or index 0 if using 0-based indexing).
Moving backward is not allowed.
Crossing the bridge means reaching beyond the last plank.

"""

class MagicalBridge:

    def solution_tabular(self, A):


        # Size of the input data
        n = len(A)

        # Create a dp array of size A to store ans
        # dp[i] = minimum steps needed from index i to cross the bridge
        dp = [float('inf') for _ in range(n)]

        for i in range(n-1, -1, -1):

            # Take normal jump and get the min junps required
            normal = 0
            if i+1 < n:
                normal = dp[i+1]
            
            # Take magical jump and check min jumps required to cross the bridge
            magical = 0
            if i + A[i] < n:
                magical = dp[i + A[i]]

            
            # Take min of both possibility and update the dp table
            dp[i] = min(normal, magical) + 1 # Additional one step to cross bridge

        return dp[0]
    
if __name__ == "__main__":

    mb = MagicalBridge()

    # Test case 1:
    A = [2, 3, 1, 1, 1]
    print(f"Mininum jumps required to cross tabular: {mb.solution_tabular(A)}")

    # Test Case 2: 
    A = [1, 2, 3, 1]
    print(f"Mininum jumps required to cross tabular: {mb.solution_tabular(A)}")



