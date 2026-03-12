"""
There are N jobs to be done, but you can do only one job at a time.

Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.

Your aim is to select jobs in such a way so that you can finish the maximum number of jobs.

Return the maximum number of jobs you can finish.
"""

class FinishMaximuJob:

    def solution_greedy(self, A: list[int], B: list[int])-> int:

        jobs = []
        # Covert to invertals (2d array)
        for i in range(0, len(A), 1):
            jobs.append([A[i], B[i]])

        jobs.sort(key= lambda x: x[1])
        # Pick the job that ends early
        ans = 1
        previous_end = jobs[0][1]
        for i in range(1, len(jobs), 1):

            current_start = jobs[i][0]

            if (previous_end <= current_start):
                ans += 1
                previous_end = jobs[i][1]

        return ans

if __name__ == "__main__":

    fmj = FinishMaximuJob()

    A = [1, 5, 7, 1]
    B = [7, 8, 8, 8]

    print(f"Maximum Jobs finished: {fmj.solution_greedy(A, B)}")
