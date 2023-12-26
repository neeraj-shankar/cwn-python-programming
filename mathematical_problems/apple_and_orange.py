"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below,
determine the number of apples and oranges that land on Sam's house.

"""


class AppleAndOrangeCount(object):
    @staticmethod
    def find_apple_and_orange_count(s, t, a, b, apples, oranges):
        apple_count = 0
        orange_count = 0

        for apple in apples:
            if s <= a + apple <= t:
                apple_count += 1

        for orange in oranges:
            if s <= b + orange <= t:
                orange_count += 1

        print(f"{apple_count}\n{orange_count}")


"""
Input data and function calls
"""

# Sam's house start and end point coordinates
first_multiple_input = input().rstrip().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

# The location of the apple and orange tree respectively
second_multiple_input = input().rstrip().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

# The number of apples and oranges fall from the respective trees
third_multiple_input = input().rstrip().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

# The fall distance coordinate from respective tree
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

AppleAndOrangeCount.find_apple_and_orange_count(s, t, a, b, apples, oranges)
