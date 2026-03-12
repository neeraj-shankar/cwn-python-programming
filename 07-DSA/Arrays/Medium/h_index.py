"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such that the given researcher has published 
at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: 
[3,0,6,1,5] means 
-------------------------------------------------
1. the researcher has 5 papers in total
2. each of them had received 3, 0, 6, 1, 5 citations respectively.

3. Since the researcher has 3 papers with at least 3 citations each and the remaining 
two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1

"""

class HIndex:

    def solution_bruteforce(self, papers)-> int:
        """
        1. For each number, check how many numbers greater than equal to it. Maintain the count
        2. If the count is greater than or equal to the number that is valid.
        3. Maintain the max of answer
        """

        n = len(papers)
        ans = 0
        for i in range(n):
            
            # Total papers with citations greater than citations of papers[i]
            count = 0
            for j in range(n):
                if (papers[j] >= papers[i]):
                    count += 1
            
            # Maximum papers with citations atleast less than/equal to of A[i]
            if count <= papers[i]:
                ans = max(ans, count)
        
        return ans;

    def solution_sorting(self, citations: list[int]) -> int:
        """
        1. Same logic as bruteforce except, count part where sorting help count easy.
        """

        n = len(citations)

        citations.sort(reverse=True)

        idx = 0

        while idx < n and citations[idx] > idx:
            idx += 1
        
        return idx
    
    def solution_optimal(self, citations: list[int])-> int:

        n = len(citations)
    
        # Create frequency array of citations count
        freq = [0 for _ in range(n+1)]

        for citation in citations:

            if citation > n:
                freq[len(freq)-1] += 1
            else:
                freq[citation] += 1
        
        # Traverse from back and return freq.
        idx = len(freq)

        count = 0
        idx = -1
        for i in range(len(freq)-1, -1, -1):

            if (freq[i] > i):
                
                return i
        
        return 0


if __name__ == "__main__":

    hi = HIndex()

    # Test case 1:
    citations = [3,0,6,1,5]
    print(f"H - Index Bruteforce: {hi.solution_bruteforce(citations)}")
    print(f"H - Index Sorting: {hi.solution_sorting(citations)}")
    print(f"H - Index Optimal: {hi.solution_optimal(citations)}")



    # Test Case 2:
    citations = [1,3,1]
    print(f"H - Index: {hi.solution_bruteforce(citations)}")
    print(f"H - Index Sorting: {hi.solution_sorting(citations)}")


    # Test case 3: Single paper
    papers = [10] # Expected: 1
    print(f"H - Index: {hi.solution_bruteforce(papers)}")
    print(f"H - Index Sorting: {hi.solution_sorting(papers)}")


    # Test case 4: Increasing
    papers = [0,1,2,3,4,5] # Expected: 3
    print(f"H - Index: {hi.solution_bruteforce(papers)}")
    print(f"H - Index Sorting: {hi.solution_sorting(papers)}")

    # Test case 5: Decreasing
    papers = [10,8,5,4,3] # Expected: 4
    print(f"H - Index: {hi.solution_bruteforce(papers)}")
    print(f"H - Index Sorting: {hi.solution_sorting(papers)}")

    # Test case 6: All same values
    papers = [5,5,5,5,5] # Expected: 5
    print(f"H - Index: {hi.solution_bruteforce(papers)}")
    print(f"H - Index Sorting: {hi.solution_sorting(papers)}")

    # Test case 7: All same values 2
    papers = [0,0,0,0,0] # Expected: 0
    print(f"H - Index: {hi.solution_bruteforce(papers)}")
    print(f"H - Index Sorting: {hi.solution_sorting(papers)}")

    # Test case  8: Trcky distributions
    papers = [25,8,5,3,3] # Expected: 3
    print(f"H - Index: {hi.solution_bruteforce(papers)}")
    print(f"H - Index Sorting: {hi.solution_sorting(papers)}")

    # Test case 9: 
    papers = [100, 99, 98, 1, 1, 1, 1]   # Expected: 3
    print(f"H - Index: {hi.solution_bruteforce(papers)}")
    print(f"H - Index Sorting: {hi.solution_sorting(papers)}")






