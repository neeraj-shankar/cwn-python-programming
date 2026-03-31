"""
Farmer John has built a new long barn with N stalls. Given an array of integers A of 
size N where each element of the array represents the location of the stall 
and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. 
To prevent the cows from hurting each other, John wants to assign the cows to the stalls, 
such that the minimum distance between any two of them is as large as possible. 

What is the largest minimum distance?
"""

class AggresiveCows:

    def solution(self, A: list, B: int)-> int:

        # length of total stalls
        n = len(A)

        low = 1
        high = A[n-1]
        max_distance = 0
        while (low <= high):

            mid = low + (high - low)//2
            if self.check(A, B, mid):
                # cows can be placed so maximize the distance
                max_distance = mid
                low = mid + 1
            else:
                # Cows cannot be placed mid distance apart so reduce the distance
                high = mid - 1

        return max_distance
    
    def check(self, positions: list, cows: int, dist: int):

        last_pos = positions[0]
        cow = 1

        for i in range(1, len(positions), 1):

            # Check if a cow can placed at current position
            if positions[i] - last_pos >= dist:

                cow += 1
                last_pos = positions[i]

                if cow == cows:
                    # print(f"Yes! All cows can fit: {dist} distance apart")
                    return True
        
        return False
    
if __name__ == "__main__":

    ac = AggresiveCows()

    # Test Case 1:
    A = [1, 2, 3, 4, 5]
    B = 3
    print(f"Maximum possible distance: {ac.solution(A, B)}")

    # Test case 2:
    A = [1, 2]
    B = 2
    print(f"Maximum possible distance: {ac.solution(A, B)}")
