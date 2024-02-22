"""
---------------------------------------------------------------------------------------------------
Problem Statement:
-------------------------------------------------
Extract values of a particular key in Nested Values 

"""
# initializing dictionary
test_dict = {
    "Gfg": {"a": 7, "b": 9, "c": 12},
    "is": {"a": 15, "b": 19, "c": 20},
    "best": {"a": 5, "b": 10, "c": 2},
}

##############################################################################
# # Question1--> Extract All values of specified key 
##############################################################################

expected_key = "some_key"

# Assuming test_dict is your dictionary
test_dict = {
    "item1": {"some_key": "value1", "another_key": "another_value1"},
    "item2": {"some_key": "value2", "another_key": "another_value2"},
    "item3": {"another_key": "another_value3"},
}

# Use list comprehension to extract values based on the condition
extracted_values = [
    v[expected_key] for k, v in test_dict.items() if expected_key in v.keys()
]

print(extracted_values)
