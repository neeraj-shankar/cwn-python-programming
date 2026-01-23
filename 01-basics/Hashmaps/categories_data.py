"""
Categorize data by a specific attribute.
-----------------------------------------------------------
The Task: You have a list of students with their names and their assigned house.
Group them so you have a dictionary where the "House Name" is the key
and the value is a list of student names.

Input
-----------------------------------------------------------
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Hermione", "house": "Gryffindor"}
]

Output: {"Gryffindor": ["Harry", "Hermione"], "Slytherin": ["Draco"]}
"""
from collections import defaultdict

class CategoriesData:

    @staticmethod
    def solution_bruteforce(students: list) -> dict:
        """
        1. Create a new dictionary for results. Go through each dictionary in list. 
        2. Exract the key--> 'house'. Check if this is present in result.
        3. If not, create a key: value in result where key is extracted key and value is a list instance
        4. Else append the value of name key.

        Time and space Complexity
        ---------------------------------------------------
        TC -> O(N) --> only visiting each item once
        SC --> O(N+N) --> At max N for keys in original list + N for list inside the dict in worst case
        """

        result = {}
        for data in students:
            key = data['house']
            if key not in result:
                result[key] = list()
            result[key].append(data['name'])

        return result

    @staticmethod
    def solution_defaultdict(students: list) -> dict:

        result = defaultdict(list)
        for data in students:
            key = data['house']
            result[key].append(data['name'])
        
        return result
    
    @staticmethod
    def solution_setdefault(students: list) -> dict:

        result = {}
        for data in students:
            key = data['house']
            result.setdefault(key, []).append(data['name'])
        print(result)

        return result

if __name__ == "__main__":

    # Create the class object
    cd = CategoriesData()

    # Test case 1:
    students = [
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Hermione", "house": "Gryffindor"},
    ]

    result = cd.solution_bruteforce(students)
    print(f"Categorised Result: ", result)
    result = cd.solution_defaultdict(students)
    print("Categorised Data using default dict: ", result)

    cd.solution_setdefault(students)


