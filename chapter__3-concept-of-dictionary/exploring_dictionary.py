###################################################################################################
##    copy () and clear() method
###################################################################################################

animal_dictonary = {
    "name": "Tiger",
    "type": "Carnivore"
}

# Using copy() method to create shallow copy
print(f"Original Dictionary address: {id(animal_dictonary)}")
shallow_animal_dictionary = animal_dictonary.copy()
print(f"Copied Dictionary: {shallow_animal_dictionary}") # Copied Dictionary: {'name': 'Tiger', 'type': 'Carnivore'}
print(f"Copied Dictionary address: {id(shallow_animal_dictionary)}")

# using clear() method to clear the shallow copied dictionary
shallow_animal_dictionary.clear()
print(f"Updated Copied Dictionary after being cleared: {shallow_animal_dictionary}")
# Updated Copied Dictionary after being cleared: {}


###################################################################################################
##    items(), keys() and values() method
###################################################################################################
    