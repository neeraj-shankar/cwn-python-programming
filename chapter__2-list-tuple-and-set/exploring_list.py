#######################################################################################################################
### Exploring the append() method
### Usage: Appends the specified element to the end of the list.
### Time Complexity: O(1) (amortized)
### Space Complexity: O(1)
#######################################################################################################################
my_list = [1, 2, 3]
print(f"Original List: {my_list}")

# Adding one element at the end
my_list.append(4)
print(f"Updated List: {my_list}")  # Updated List: [1, 2, 3, 4]

# Adding tuple to the list
my_tup = (5, 6)
my_list.append(my_tup)
print(
    f"Updated list after tuple append: {my_list}"
)  # Updated list after tuple append: [1, 2, 3, 4, (5, 6)]

# adding dictionary to a list
my_dictionary = {"name": "Neeraj", "code": 1, "status": False}

my_list.append(my_dictionary)
print(f"Updated list after dictionary addition: {my_list}")
# Updated list after dictionary addition: [1, 2, 3, 4, (5, 6), {'name': 'Neeraj', 'code': 1, 'status': False}]

# adding set to existing list
my_set = {1, 2, 3, 4}
my_list.append(my_set)
print(f"Updated List after set append: {my_list}")
# Updated List after set append: [1, 2, 3, 4, (5, 6), {'name': 'Neeraj', 'code': 1, 'status': False}, {1, 2, 3, 4}]


#######################################################################################################################
### Exploring the extend() method
### Usage: Appends elements from the iterable to the end of the list.
### Time Complexity: O(k), where k is the length of the iterable.
### Space Complexity: O(k)
#######################################################################################################################
print(
    f"============================================================================================="
)
print(f"Exploring the extend method")
print(
    f"============================================================================================="
)
original_list = [1, 2, 3]
print(f"Original List: {original_list}")

# adding a list using extend
new_list = [4, 5]
original_list.extend(new_list)
print(f"Updated list: {original_list}")  # Updated list: [1, 2, 3, 4, 5]

# trying to add single element using extend
try:
    new_element = 6
    original_list.extend(new_element)
    print(f"Updated list after adding single element: {original_list}")
    #  TypeError: 'int' object is not iterable
except TypeError as error:
    print(f"Single element cannot be added: {error}")

# adding tuple to a list using extend
new_tuple = (6, 7)
original_list.extend(new_list)
print(f"Updated List after extending tuple: {original_list}")
# Updated List after extending tuple: [1, 2, 3, 4, 5, 4, 5]

# Trying to add string element using extend
new_str = "Neeraj"
original_list.extend(new_str)
print(f"Updated list after extending string: {original_list}")
# Updated list after extending string: [1, 2, 3, 4, 5, 4, 5, 'N', 'e', 'e', 'r', 'a', 'j']

# Trying to add single char to list using extend
new_chr = "U"
original_list.extend(new_chr)
print(f"Update list after adding single char: {original_list}")
# Update list after adding single char: [1, 2, 3, 4, 5, 4, 5, 'N', 'e', 'e', 'r', 'a', 'j', 'U']

# Adding a dictionary to existing list using extend
new_dictionary = {"name": "Neeraj", "code": 2, "status": True}

original_list.extend(new_dictionary)
print(f"Updated List after adding dictionary: {original_list}")
# Updated List after adding dictionary: [1, 2, 3, 4, 5, 4, 5, 'N', 'e', 'e', 'r', 'a', 'j', 'U', 'name', 'code', 'status']

#######################################################################################################################
### Exploring the insert(index, element): method
### Usage: Inserts the specified element at the specified position in the list.
### Time Complexity: O(n), where n is the length of the list.
### Space Complexity: O(1)
#######################################################################################################################
insert_list = [
    "Neeraj",
    True,
    1,
]
print(
    f"==========================================================================================="
)
print(f"Original List: {insert_list}")


try:
    insert_list.index(3, "Shankar")
    print(f"Updated list after insertion at non existent index:{insert_list}")
    # TypeError: slice indices must be integers or have an __index__ method
except TypeError as err:
    print(f"Error Message: {err}")
except Exception as e:
    print(f"Unknown Exception Handling: {e}")

insert_list.insert(1, 2)
print(f"Updated list after adding at known index: {insert_list}")
# Updated list after adding at known index: ['Neeraj', 2, True, 1]

# Insterting a tuple a list

insert_tuple = (1, 2, 3)
insert_list.insert(0, insert_tuple)
print(f"updated list after Tuple insert: {insert_list}")
# TypeError: insert expected 2 arguments, got 1

# Inserting a list to a list
insert_elist = [1, 2, 3]
insert_list.insert(0, insert_elist)
print(f"Updated list after list insert: {insert_list}")

# Inserting dictionary to a list
insert_dictionary = {"name": "Sample", "id": 12345, "status": False}
insert_list.insert(0, insert_dictionary)
print(f"Updated list after dictionay insert: {insert_dictionary}")
# Updated list after dictionay insert: {'name': 'Sample', 'id': 12345, 'status': False}

# Inserting a set to a list
insert_set = {0, 1, 2}
insert_list.insert(0, insert_set)
print(f"Updated list after set insert: {insert_list}")
# Updated list after set insert: [{0, 1, 2}, {'name': 'Sample', 'id': 12345, 'status': False}, [1, 2, 3], (1, 2, 3), 'Neeraj', 2, True, 1]

#######################################################################################################################
### Exploring the remove(element): method
### Usage: Removes the first occurrence of the specified element from the list.
### Time Complexity: O(n), where n is the length of the list.
### Space Complexity: O(1)
#######################################################################################################################
remove_list = [1, "Sample", True, False, "2", "delete", "avoid", (1, 2), [1, 2], {"name": "Sample"}, {1, 2, 3}, ]
print(f"Original Removal list: {remove_list}")
remove_list.remove(0)
print(f"Updated list after first Invalid removal: {remove_list}")
# it does not remove element by index
# Updated list after first removal: [1, 'Sample', True, '2', 'delete', 'avoid', (1, 2), [1, 2], {'name': 'Sample'}, {1, 2, 3}]

remove_list.remove(1)
print(f"Updated list after first removal: {remove_list}")
# Updated list after first removal: ['Sample', True, '2', 'delete', 'avoid', (1, 2), [1, 2], {'name': 'Sample'}, {1, 2, 3}]
