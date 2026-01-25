"""
You are given a collection of intervals A in a 2-D array format, 
where each interval is represented by a pair of integers `[start, end]`. 

The intervals are sorted based on their start values.
Your task is to merge all overlapping intervals and return the resulting set of non-overlapping intervals.
"""

class MergeSortedIntervals():

    def solution(self, A):
        """
        1. As the given intervals are already sorted based on start time.
        2. Using the concept that two intervals can only overlap if
            a. s1 <= e2  and
            b. s2 <= e2 

        3. We can say, two intervals are non-overalpping if:
           a. e1 < s2 or
           b. e2 < s1
        """

        ans = []
        n = len(A)
        # Base Case: Empty intervals or when there is only one interval
        if n <= 1: return A

        li = A[0]
        for i in range(1, n):
            ci = A[i]

            if (li[0] <= ci[1] and ci[0] <= li[1]):
                li[1] = max(li[1], ci[1])
            else:
                ans.append(li)
                li = ci 
        # At last add the remaining interval
        ans.append(li)
        return ans



if __name__ == "__main__":

    msi = MergeSortedIntervals()

    A = [ [1, 3], [2, 6], [8, 10], [15, 18] ]

    print(f"Merged Intervals: {msi.solution(A)}")