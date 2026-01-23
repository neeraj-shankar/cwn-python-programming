"""

Swapping keys and values.
-----------------------------------------------------------
Given a dictionary where names are keys and their favorite colors are values, create a new dictionary 
where the colors are the keys and the values are the names.

If two people have the same favorite color, the value should be a list of names so you don't lose data!

Input: {"Alice": "Blue", "Bob": "Green", "Charlie": "Blue"}

Output: {"Blue": ["Alice", "Charlie"], "Green": ["Bob"]}
"""

class Invert():

    @staticmethod
    def solution_bruteforce(hm: dict)-> dict:
        """
        1. Create a new result dictionary, visit each key value pair in input data
        2. Check if the key with color exists in result dictionary 
        3. if Exists --> just the append the name as value to the color key
        4. Else create a new value of list and add the name to it
        """
        result = {}

        for key, val in hm.items():

            if val not in result:
                # Initialize a list 
                result[val] = list()
            result[val].append(key)

        return result
    
    @staticmethod 
    def solution_setdefault(hm: dict) -> dict:

        result = {}
        for name, color in hm.items():

            result.setdefault(color, []).append(name)

        print(result)

    @staticmethod
    def solution_defaultdict(hm: dict) -> dict:
        from collections import defaultdict
        result = defaultdict(list)
        for name, color in hm.items():
            result[color].append(name)
        print(result)


if __name__ == "__main__":

    hm = {"Alice": "Blue", "Bob": "Green", "Charlie": "Blue"}

    result = Invert.solution_bruteforce(hm)
    print("Inverted Output: ", result)

    Invert.solution_setdefault(hm)
    Invert.solution_defaultdict(hm)
