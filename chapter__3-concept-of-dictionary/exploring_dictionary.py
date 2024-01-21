###################################################################################################
##    copy () and clear() method
###################################################################################################
print("--" * 50)
animal_dictonary = {"name": "Tiger", "type": "Carnivore"}

# Using copy() method to create shallow copy
print(f"Original Dictionary address: {id(animal_dictonary)}")
shallow_animal_dictionary = animal_dictonary.copy()
print(
    f"Copied Dictionary: {shallow_animal_dictionary}"
)  # Copied Dictionary: {'name': 'Tiger', 'type': 'Carnivore'}
print(f"Copied Dictionary address: {id(shallow_animal_dictionary)}")

# using clear() method to clear the shallow copied dictionary
shallow_animal_dictionary.clear()
print(f"Updated Copied Dictionary after being cleared: {shallow_animal_dictionary}")
# Updated Copied Dictionary after being cleared: {}


###################################################################################################
##    items(), keys() and values() method
###################################################################################################
print("--" * 50)
# Nested dictionary representing student grades in different subjects
student_grades = {
    "Alice": {"Math": 90, "English": 85, "Science": 92},
    "Bob": {"Math": 88, "English": 92, "Science": 89},
    "Charlie": {"Math": 95, "English": 78, "Science": 87},
}


# items() returns a view object that displays a list of dictionary's key-value tuple
for name, grades in student_grades.items():
    print(f"Student Number: {name}, Student Detail: {grades}")


# keys() returns a view object that displays a list of dictionary keys.
print("**" * 30)
student_name = "Bob"
if student_name in student_grades.keys():
    print(f"Grades details for student: {student_name}")
    for subject in student_grades[student_name].keys():
        print(f"{subject}: {student_grades[student_name][subject]}")
