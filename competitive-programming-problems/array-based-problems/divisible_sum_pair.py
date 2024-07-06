"""
---------------------------------------------------------------------------------------------------
Problem Statement:
-------------------------------------------------
Given an array of integers and a positive integer , k determine the number of  pairs (i,j) wherei <j
and arr[i] + arr[j] is divisible by k.

Example Input
-------------------------------------------------
arr = [1, 2, 3, 4, 5, 6]
k = 5

Example Output:
-------------------------------------------------
Total Maching Pair: 3

Explanation:
-------------------------------------------------
Three Pairs matches the criteria: [1, 4], [2, 3] and [4, 6]

---------------------------------------------------------------------------------------------------

"""


def count_divisible_pairs(arr, k):
    """
    Takes arr and postive iteger, returns the number of possible pairs
    matching problem statement.

    Param: arr: The input array to be evaluated
    Param: k: The postive integer to check if pairs are divisible it.
    Returns: Pair Count
    Time Complexity: O(n)2
    Space Complexity: O(1)
    """

    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % k == 0:
                count += 1

    return count


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 6]
    k = 5
    result = count_divisible_pairs(test_arr, k)
    print(f"Total Matching Pair: {result}")


"""
More Efficient Approach to the problem using Hash Map (dictionary in python)
"""


def count_pairs(arr, k):
    remainder_count = {}
    count = 0

    for num in arr:
        remainder = num % k
        complement = (
            k - remainder
        ) % k  # Calculate the complement to make the sum divisible by k

        # Check if the complement is present in the remainder_count
        count += remainder_count.get(complement, 0)
        print(f"Count of Pairs: {count}")

        # Update the remainder_count
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        print(f"Remainder Count: {remainder_count}")

    return count


# Example usage:
arr = [1, 2, 3, 4, 5, 6]
k = 5

result = count_pairs(arr, k)
print(result)
