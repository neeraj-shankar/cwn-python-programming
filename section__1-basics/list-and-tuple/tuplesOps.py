nums = (1, 3, 2, 4, 3, 2)
import sys
# get the element by index
print(nums[1])
print(nums.index(2, 3, len(nums)))
print(nums.count(3))

nums = [1, 2, 2, 3, 4, 5, 2, 2, 2, 2]
print(nums.count(2))
print(f"Actual size of list: ")
print(sys.getsizeof(nums))

# use of list comprehension
odd_nums = [x for x in nums if (x % 2 == 1)]
print(f"Odd Numbers: {odd_nums}")

# Tuples in a set
my_set = {1, 2, "Neeraj"}
my_set.add((1, 2,))
print(f"Set: {my_set}")

