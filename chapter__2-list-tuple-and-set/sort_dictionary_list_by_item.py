"""
Ways to sort list of dictionaries by values in Python – Using itemgetter
"""
from operator import itemgetter
"""
What is Itemgetter in Python?
--------------------------------------------------------------------------------------------------------------------
The Itemgetter can be used instead of the lambda function to achieve similar functionality. Outputs in the same way as 
sorted() and lambda, but has different internal implementation. It takes the keys of dictionaries and converts them 
into tuples. It reduces overhead and is faster and more efficient. The “operator” module has to be imported for its 
work. The code is explained below 

Performance: itemgetter performs better than lambda functions in the context of time.
Concise: : itemgetter looks more concise when accessing multiple values than lambda functions.
"""


def sort_dictionary_list(input_dict_list):
    result = sorted(input_dict_list, key=itemgetter("age", "name"))
    print(f"The sorted list of dictionary --> {result}")


"""
Input data and function call
"""

dict_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]
sort_dictionary_list(dict_list)
