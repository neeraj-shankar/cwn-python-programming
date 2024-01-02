Overview
-----------------------------------------------------------------------------------------------------------------------
dictionaries are versatile data structures that allow you to store key-value pairs. Here are some of the commonly used 
methods associated with dictionaries:

1. clear():
-----------------------------------------------------------------------------------------
Purpose: Removes all elements from the dictionary.
Time Complexity: 
Space Complexity:

2. copy():
-----------------------------------------------------------------------------------------
Purpose: Returns a shallow copy of the dictionary.
Time Complexity: 
Space Complexity:

3. get(key, default=None):
-----------------------------------------------------------------------------------------
Purpose: Returns the value for the given key if it exists; otherwise, returns the default value.
Time Complexity: 
Space Complexity:

4. items():
-----------------------------------------------------------------------------------------
Purpose: Returns a view object that displays a list of a dictionary's key-value tuple pairs.
Time Complexity: 
Space Complexity:

5. keys():
-----------------------------------------------------------------------------------------
Purpose: Returns a view object that displays a list of all the keys in the dictionary.
Time Complexity: 
Space Complexity:

6. values():
-----------------------------------------------------------------------------------------
Purpose: Returns a view object that displays a list of all the values in the dictionary.
Time Complexity: 
Space Complexity:

7. pop(key, default=None):
-----------------------------------------------------------------------------------------
Purpose: Removes the key-value pair for the given key and returns its value. If the key is not found, it returns the 
default value or raises a KeyError if no default is provided.
Time Complexity: 
Space Complexity:

8. popitem():
-----------------------------------------------------------------------------------------
Purpose: Removes and returns a (key, value) pair from the dictionary. Raises a KeyError if the dictionary is empty.
Time Complexity: 
Space Complexity:

9. setdefault(key, default=None):
-----------------------------------------------------------------------------------------
Purpose: Returns the value for the given key if it exists; otherwise, sets the key to the default value and returns it.
Time Complexity: 
Space Complexity:

10. update(iterable/another_dictionary):
-----------------------------------------------------------------------------------------
Purpose: Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
Time Complexity: 
Space Complexity:

11. fromkeys(iterable, value=None):
-----------------------------------------------------------------------------------------
Purpose: Creates a new dictionary with keys from an iterable and values set to the provided value (default is None).
Time Complexity: 
Space Complexity:

12. contains(key):
-----------------------------------------------------------------------------------------
Purpose: Checks if the dictionary contains the specified key. This method is often used implicitly with the in keyword.
Time Complexity: 
Space Complexity:

13. iter():
-----------------------------------------------------------------------------------------
Purpose: Returns an iterator over the dictionary's keys. This method is used when you loop over a dictionary without 
explicitly calling keys().
Time Complexity: 
Space Complexity:

