"""
You have a set of non-overlapping intervals. You are given a new interval [start, end], 
insert this new interval into the set of intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

class InsertIntervals():

    
    def solution(self, A, B):
        """
        1. Create an answer 2d- array.
        2. Add all the intervals that end before the incoming intervals
        3. Merge the incoming intervals 
        4. Verify and ensure all intervals are non-overlapping after insertion
        """
        
        ans = []
        i = 0 
        n = len(A)
        # Insert all the intervals that end before B to answer
        while(i < n and A[i][1] < B[0]):
            ans.append(A[i])
            i += 1

        # print(f"Answer after all intervals that ended before: {ans} and i is {i}")
        # Now merge overlapping intervals with incoming interval
        while(i < n and (A[i][0] <= B[1] and B[0] <= A[i][1])):
            B[0] = min(A[i][0], B[0])
            B[1] = max(A[i][1], B[1])
            i += 1

        ans.append(B)
        # print(f"Answer after merge: {ans} and i is {i}")
        # Add remaining intervals to the ans
        while(i < n):
            ans.append(A[i])
            i += 1

        return ans 

if __name__ == "__main__":
    obj = InsertIntervals()

    # # Test case 1: Generic
    # A = [[1, 3], [6, 9]]
    # B = [2, 5]
    # print(f"Intervals after insertion: {obj.solution(A, B)}")

    # # Test Case 2: 
    # A = [[1, 3], [6, 9]]
    # B = [2, 6]
    # print(f"Intervals after insertion: {obj.solution(A, B)}")

    # Test Case 3:
    A = [[1,2],[3,6]]
    B = [8,10]
    print(f"Intervals after insertion: {obj.solution(A, B)}")



