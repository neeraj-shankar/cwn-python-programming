"""
---------------------------------------------------------------------------------------------------
Problem Statement: 
Each of the squares has an integer on it. Lily decides to share a contiguous segment of the bar 
selected such that:
1. The length of the segment matches Ron's birth month, and,
2. The sum of the integers on the squares is equal to his birth day.

Problem Statement with regards programming:
-------------------------------------------------
Finding a contiguous segment of an array (or a list in Python) that satisfies specific conditions
regarding its length and the sum of its elements. 

Example Input:
-------------------------------------------------
s = [2, 2, 1, 3, 2]
d= 4
m = 4

Example Output:
-------------------------------------------------
The number of ways bar can be divided: 2

Explanation
-------------------------------------------------
Here m = 2, the length of Contiguous Segment (length of subarray). But the same of element of the
subarray should be equal to 4. So there are two possible ways, [2, 2,] and [1, 3]

---------------------------------------------------------------------------------------------------
"""


def birthday_chocolate(chocolate_bar, month, date):
    count = 0

    for i in range(0, len(chocolate_bar) - month + 1):
        segment = chocolate_bar[i : i + month]
        print(f"Segement: {segment}")
        if sum(segment) == date:
            count += 1
    return count


if __name__ == "__main__":
    chocolate_bar = [2, 2, 1, 3, 2]
    birth_month = 2
    birth_date = 4

    result = birthday_chocolate(chocolate_bar, birth_month, birth_date)
    print(f"The Number of ways Chocolate can be distributed: {result}")
