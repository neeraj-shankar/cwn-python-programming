"""
A subnumber is defined as any number formed by selecting a subset of digits from N while 
maintaining their original relative order. You may choose any non-empty subset of digits.

Your task is to find the subnumber whose numeric value is closest to K.
"""

class ClosestSubNumber:

    @classmethod
    def solve(cls, number: int, target: int):

        # Convert the number to a list 
        x = number
        nums = []
        while x > 0:
            
            digit = x % 10
            x = x // 10
            nums.append(digit)
        print(nums)

        nums = nums[::-1]
        print(nums)

    def subset():
        pass
if __name__ == "__main__":

    csn = ClosestSubNumber()

    # Test case1
    number = 123
    k = 14
    print(f"Closest number: {csn.solve(number, k)}")

