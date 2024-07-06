"""
From an array of string (list in cases of python)  return the third largest string from the array
"""
from format_output import  use_case_separator


class LargestStringEvaluation:

    # the input list of strings
    str_arr = ["hello", "world", "before", "all"]

    """
    find the third-largest string from list of strings
    """
    def third_largest_string(self):

        print(f"The original list of strings --> {self.str_arr}")
        # sort the strings in the list in ascending order by their length
        sorted_str_arr = sorted(self.str_arr, key=len, reverse=True)
        print(f"The list of string in descending order --> {sorted_str_arr}")

        return sorted_str_arr[2]


"""
Object creation and funtion calls
"""
tes_obj = LargestStringEvaluation()

use_case_separator()
print(f"The third largest string is -->{tes_obj.third_largest_string()}")
