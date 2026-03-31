# Regular function - creates entire list in memory
def get_numbers_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

numbers = get_numbers_list(1000000)  # Creates 1 million numbers immediately!
print(numbers)
# Generator - produces values one at a time
def get_numbers_generator(n):
    for i in range(n):
        yield i * i  # 'yield' is the magic keyword

numbers = get_numbers_generator(1000000)  # Creates nothing yet!
print(numbers.__next__())
print(numbers.__next__())


import sys

# List comprehension - creates everything
list_comp = [x * x for x in range(1000000)]
print(f"List size: {sys.getsizeof(list_comp)} bytes")  # ~8 MB

# Generator expression - creates almost nothing
gen_exp = (x * x for x in range(1000000))
print(f"Generator size: {sys.getsizeof(gen_exp)} bytes")  # ~200 bytes!