"""
A python program to show different ways to swapping a nested dictionary """

from format_output import use_case_separator


class DictionarySwap:

    # test dictionary sample data
    test_dict = {"Neeraj": {"workout1": ["Mon", "Tue", "Wed"], "workout2": ["Thurs", "Fri", "Sat"]},
                 "Ankit": {"workout1": ["Mon", "Tue"], "workout2": ["Thurs", "Sat"], "workout3": ["Sun", "only 7daya"]}
                 }

    def using_loop_and_items(self):
        refactored_dict = dict()
        print(f"newly created dict --> {refactored_dict}")
        for key, val in self.test_dict.items():
            print(f"The key status --> {key}")
            print(f"The items status --> {val}")
            for key_in, val_in in val.items():
                print(f"The sub key status --> {key_in}")
                print(f"The sub items status --> {val_in}")
                if key_in not in refactored_dict:
                    temp = dict()
                else:
                    temp = refactored_dict[key_in]
                    temp[key] = val_in
                    refactored_dict[key_in] = temp
        print(f"The swapped version of dictionary --> {refactored_dict}")



"""
Create object and function calls
"""
test_obj = DictionarySwap()

use_case_separator()
test_obj.using_loop_and_items()

#
# test_dict = {'Gfg': {'a': [1, 3], 'b': [3, 6], 'c': [6, 7, 8]},
#              'Best': {'a': [7, 9], 'b': [5, 3, 2], 'd': [0, 1, 0]}}

test_dict = {"Neeraj": {"workout1": ["Mon", "Tue", "Wed"], "workout2": ["Thurs", "Fri", "Sat"]},
                 "Ankit": {"workout1": ["Mon", "Tue"], "workout2": ["Thurs", "Sat"], "workout3": ["Sun", "only 7daya"]}
                 }

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Swapping Hierarchy in Nested Dictionaries
# Using loop + items()
res = dict()
for key, val in test_dict.items():
    for key_in, val_in in val.items():
        if key_in not in res:
            temp = dict()
        else:
            temp = res[key_in]
        temp[key] = val_in
        res[key_in] = temp

# printing result
print("The rearranged dictionary : " + str(res))



