"""
You are given:

An array boards[] of size n, where each element represents the length of a board.
An integer k, representing the number of painters available.
🧱 Rules:
Each painter can only paint continuous boards (i.e., a contiguous segment of the array).
A board cannot be split between multiple painters.
All painters work at the same rate (1 unit length = 1 unit time).
Each painter paints only one continuous section.
"""

class PaintersPartition:
    
    def solution(self, boards, painters):
        
        n = len(boards)
        
        # Search space 
        total_length = 0
        max_length = float('-inf')
        for board in boards:
            total_length += board
            
            max_length = max(max_length, board)
            
        
        low = max_length
        high = total_length
        ans = float('inf')
        while (low <= high):
            mid = (low + high)//2
            
            ptrs = self.painters(boards, mid)
            
            if ptrs <= k:
                ans = mid 
                high = mid -1
            else:
                low = mid + 1
                
        return ans 
    def painters(self, boards, tt):
        
        n = len(boards)
        
        tl = tt - boards[0]
        painter_count = 1
        for i in range(1, n):
            
            tr = boards[i]
            
            if tr <= tl:
                tl -= tr 
            else: 
                painter_count += 1 
                tl = tt - tr 
                
        return painter_count
        
if __name__ == "__main__":
    
    pp = PaintersPartition()
    
    # Test  Case 
    boards = [10, 20, 30, 40]
    k = 2
    print(f"Minimum Time required: {pp.solution(boards, k)}")
    
    