"""
A python program to find all the values associated with a given key in nested python dictionary
"""
from format_output import use_case_separator


class ValueRetrievalNestedDictionary:
    test_data = {
        'Gfg': {"a": 7, "b": 9, "c": 12},
         'is': {"a": 15, "b": 19, "c": 20},
         'best': {"a": 5, "b": 10, "c": 2}
    }

    """
    Using the list comprehension
    """
    def fetch_given_key_value(self):
        temp = "a"
        resultant_data = [val[temp] for key, val in self.test_data.items() if temp in val]
        print(f"The extracted value for key --> {temp} --> {resultant_data}")

    """
    Using the naive approach 
    """
    def using_looping_approach(self):
        result_data = []

        for key, value in self.test_data.items():
            print(f"The key status from test data outer loop --> {key}")
            print(f"The value status form test data outer loop --> {value}")
            for sub_key, sub_value in value.items():
                print(f"The key status from test data inner loop --> {sub_key}")
                print(f"The value status form test data inner loop --> {sub_value}")
                if sub_key == "a":
                    result_data.append(sub_value)

        print(f"The extracted data from nested dictionary --> {result_data}")
        # [7, 15, 5]


"""
Function calls and object creation
"""
test_obj = ValueRetrievalNestedDictionary()

use_case_separator()
test_obj.fetch_given_key_value()

use_case_separator()
test_obj.using_looping_approach()


