"""  
Sometimes, while working with Python strings, we can have a problem in which we need to extract the substrings 
between certain characters that can be bracketed. This can have application in cases we have tuples embedded in string
"""
import re
from format_output import use_case_separator


class SubStringExtraction:

    # class variables for testing purpose
    input_string = "A hybrid framework(pytest and selenium) is very effective for testing (automated)"

    """ 
    Extract substring inside the round bracket using regex
    Time complexity: O(n), where n is the length of the input string test_str.
    Auxiliary space: O(m), where m is the number of matches of the pattern r’\(.*?\)’ in the input string test_str.
    """
    def extract_using_regex(self):
        extracted_substring = re.findall(r'\(.*?\)', self.input_string)
        print(f"The substring inside the brackets are --> {extracted_substring}")
    

""" 
Create object and call different methods for extracting the substring
"""
test_obj = SubStringExtraction()

use_case_separator()
test_obj.extract_using_regex()
