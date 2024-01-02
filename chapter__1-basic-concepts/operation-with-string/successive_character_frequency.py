"""
Sometimes, while working with Python strings, we can have a problem in which we need to find the frequency of next
character of a particular word in string.
"""
import re

from format_output import use_case_separator


class SuccessiveCharacterSearch:

    first_input_string = 'geeksforgeeks is best for geeks. A geek should take interest.'

    """
    with use of loop, count
    """
    def using_loop_count_find(self):
        print(f"The original string --> {self.first_input_string}")

        # initializing the queue work
        que_word = "geek"

        temp = []
        for char in re.findall(que_word + ".", self.first_input_string):
            temp.append(char[-1])

        print(f"I dont know --> {temp}")
        result = {que_word: temp.count(que_word) for que_word in temp}
        print(f"{result}")


"""
Function calls and objects
"""
test_obj = SuccessiveCharacterSearch()

use_case_separator()
test_obj.using_loop_count_find()
