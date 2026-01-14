

class SecondLargest:

    def __init__(self):
        pass

    @staticmethod
    def solution_optimized(nums: list):
        """
        Keep track of two variables: first (largest) and second (second largest)
        For each element:

            1. If greater than first, update both
            2. If between first and second, update second
        """

        first = second = float('-inf')

        for idx, num in enumerate(nums):

            if num < first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        
        return None if second == float('-inf') else second

if __name__ == "__main__":
    nums =[10, 5, 20, 8, 15]
    print(SecondLargest.solution_optimized(nums))
            
            