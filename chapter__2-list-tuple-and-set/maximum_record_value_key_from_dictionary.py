"""
A python program to find the key and its value with max values
we need to find the key with maximum value of a particular key of nested records in list.
"""
from format_output import use_case_separator


class MaxValueRecords:

    # test data variable
    test_dict = {'first_sem': {'Neeraj': 29, 'Asati': 10},
                 'second_sem': {'Neeraj': 8, 'Asati': 9},
                 'third_sem': {'Neeraj': 10, 'Asati': 15}}
    """
    using looping approach to achieve this
    """
    def find_key_with_max_value(self):

        input_sub_key = "Neeraj"
        result_key = None
        max_grade = 0

        for key in self.test_dict:
            if self.test_dict[key][input_sub_key] > max_grade:
                max_grade = self.test_dict[key][input_sub_key]
                result_key = key

        print(f"The required semester is --> {result_key}")
     
    def find_max_value_key_using_lambda(self):

        input_sub_key = "Ankit"
        result_key = None
        max_grade = 0


"""
CREATE OBJECT AND FUNCTION CALLS
"""
test_obj = MaxValueRecords()

use_case_separator()
test_obj.find_key_with_max_value()



