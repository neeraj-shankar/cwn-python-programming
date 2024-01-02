"""
A Python program to understand various set operation and its use cases
"""


#####################################################################################################################
# Adding an item the existing set
#####################################################################################################################
def use_case_separator():
    print(f"\n========================================================================================================")


people_set = {"Neeraj", "Ankit", "Ankit"}
use_case_separator()
print(f"The list of people in the set --> {people_set}")
people_set.add("Ankit-2")
print(f"The updated list of people --> {people_set}")


#####################################################################################################################
# Union operation with sets
#####################################################################################################################
people_set = {"Jay", "Neeraj"}
vampire_set = {"Ankit", "Niraj"}
dracula_set = {"Gulshan", "Singh"}

people_and_vampire_together = people_set.union(vampire_set)
use_case_separator()
print(f"This is the union of the vampire and people --> {people_and_vampire_together}")

#####################################################################################################################
# Intersection operation with sets
#####################################################################################################################
people_set = {"Jay", "Neeraj"}
vampire_set = {"Ankit", "Neeraj"}
dracula_set = {"Gulshan", "Singh"}

common_in_people_and_vampire_set = people_set.intersection(vampire_set)
use_case_separator()
print(f"This is the intersection of the vampire and people --> {common_in_people_and_vampire_set}")
