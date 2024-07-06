"""
Python Program to find fibonnaci series using recursion
"""

def find_fibbonaci_series(num):
    assert num >= 0 and int(num) == num, "The number must be a postive integer"
    if num in [0,1]:
        return num
    return find_fibbonaci_series(num-1) + find_fibbonaci_series(num-2)

result = find_fibbonaci_series(35)
print(result)