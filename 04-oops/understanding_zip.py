
# Using Zip to combine two list
names = ["Alice", "Bob", "Peter"]
ages = [18, 34, 27]

combined_data = zip(names, ages) # Returns Zip Object
print(combined_data)
result = list(combined_data) # converts zip object to a list 
print(result) # [('Alice', 18), ('Bob', 34), ('Peter', 27)]
 

"""
-----------------------------------------------------------------------------------------------------------------------
Using zip in for loop to iterate over 2 iterables
-----------------------------------------------------------------------------------------------------------------------
"""
for name, age in zip(names, ages):
    print(f"{name} is {age} years old in 2023.")


"""
-----------------------------------------------------------------------------------------------------------------------
Combining two iterables with different length

Case1: first iterable is shorter
Case2: First Iterable is longer
-----------------------------------------------------------------------------------------------------------------------
"""
names = ["Alice", "Peter", "Nicholas"]
ages = [18, 28, 34, 21, 23, 45]

combined_data = list(zip(names, ages))
print(combined_data) # [('Alice', 18), ('Peter', 28), ('Nicholas', 34)]

# looping through each of above list
for name, age in zip(names, ages):
    print(f"{name} is {age} years old now.")

age_first = list(zip(ages, names))
print(age_first) # [(18, 'Alice'), (28, 'Peter'), (34, 'Nicholas')]