"""
Combining data with arithmetic.
-----------------------------------------------------------
You have two dictionaries representing "Inventory" from two different warehouses. 
Merge them into one master inventory. If an item exists in both, sum the quantities.

Input: * 
-----------------------------------------------------------
wh_1 = {"apples": 10, "bananas": 5}
wh_2 = {"apples": 3, "orange": 8}

Output
-----------------------------------------------------------
{"apples": 13, "bananas": 5, "orange": 8}
"""
from collections import Counter

class InventoryMerge():

    @staticmethod
    def solution_bruteforce(A: dict, B: dict) -> dict:
        """
        1. Create a new result dictionary, add all items from A to it.
        2. Get the items from second dictionary, check if key exists in result
        3. If key exists, just add value to existing key else create and insert new key value pair.
        """
        # result = {}
        # result.update(A)
        result = A.copy()
        
        for key, val in B.items():
            if key not in result:
                result[key] = val 
            else: 
                result[key] +=val

        return result
        
    @staticmethod
    def solution_cleaner(A: dict, B: dict) -> dict:
        """
        Same as bruteforce except using of setdefault
        """

        result = A.copy()

        for key, val in B.items():
            result[key] = result.get(key, 0) + val
        
        return result
    
    @staticmethod
    def solution_counter(A: dict, B: dict) -> dict:
        """
        Using in built class Counter from collections
        """

        result = Counter(A) + Counter(B)
        print(result)
        return result

if __name__ == "__main__":

    A = {"apples": 10, "bananas": 5}
    B = {"apples": 3, "orange": 8}

    result = InventoryMerge.solution_bruteforce(A, B)
    print("Merged Result Bruteforce: ", result)


    result = InventoryMerge.solution_cleaner(A, B)
    print("Merged Result Clean: ", result)

    InventoryMerge.solution_counter(A, B)

"""
Initialization
-----------------------------------------------------------
1. Fastest. A.copy() is a highly optimized C-call that clones memory quickly.
2. Slower. Counter(A) has to call the __init__ method, which iterates through A to validate it.

The Merge
-----------------------------------------------------------
1. Fast. You iterate through B once and perform $O(1)$ lookups.
2. Fastest. The + operator for Counters is written in optimized C.

If your data is already in standard dictionaries, the conversion time usually makes Counter 
slower than a simple loop. If your data stays as Counter objects throughout your app, Counter is faster.

Space Complexity Analysis
-----------------------------------------------------------
This is where the standard loop usually wins.
Standard Loop: 
$O(N + M)$. You create one new dictionary (result) that grows to hold the combined keys.

Counter Addition: 
$O(N + M)$ but with higher peaks. Because you are creating Counter(A) and Counter(B) as intermediate 
objects in memory before they are added together, you are briefly using significantly more RAM.
"""