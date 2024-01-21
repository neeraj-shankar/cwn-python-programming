"""
---------------------------------------------------------------------------------------------------

Problem Statement:
-------------------------------------------------
Given an array of bird sightings where every element represents a bird type id, determine the id of
the most frequently sighted type. 

If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Sample Input:
-------------------------------------------------
arr = [1, 1, 2, 2, 3]

Sample Output:
-------------------------------------------------
Bird Id with Maximum Time Sighted: 1

Explanation:
-------------------------------------------------
Birds with ID 1 and 2 are sighted most and equal number of times but Bird with Smaller ID is 1

---------------------------------------------------------------------------------------------------
"""


def most_frequent_bird(arr):
    """
    Find the bird type id that is most frequently sighted in the given array.

    Parameters:
    - arr (list): A list of bird type ids.

    Returns:
    - int: The id of the most frequently sighted bird type. If multiple types
           have the maximum frequency, return the smallest id among them.

    Time Complexity:
    - O(n), where n is the length of the input array.

    Space Complexity:
    - O(k), where k is the number of unique bird types. In the worst case,
      each bird type may have its own entry in the bird_count dictionary.

    Example:
    >>> bird_sightings = [1, 2, 3, 2, 1, 3, 4, 4, 4]
    >>> most_frequent_bird(bird_sightings)
    4
    """
    bird_count = {}
    max_count = 0
    most_frequent_bird_id = float("inf")  # Initialize with positive infinity

    for bird_id in arr:
        bird_count[bird_id] = bird_count.get(bird_id, 0) + 1

        if bird_count[bird_id] > max_count or (
            bird_count[bird_id] == max_count and bird_id < most_frequent_bird_id
        ):
            max_count = bird_count[bird_id]
            most_frequent_bird_id = bird_id

    return most_frequent_bird_id


if __name__ == "__main__":
    test_data = [3, 3, 1, 1, 2, 2]
    result = most_frequent_bird(test_data)
    print(f"Most Frequently Sighted Bird: {result}")
