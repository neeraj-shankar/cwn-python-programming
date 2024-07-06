""" 
Sometimes, while working with Python strings, we can have a problem in which we require to extract all the elements of
string except those which present in a substring.
"""


class CharacterExtraction:

    # class variable for inout string
    input_string = "geeksforgeeks is best"
    substring = "fes"

    def extract_using_loop_way(self):

        resultant_string = []
        print(f"The empty list --> {resultant_string} and the type --> {type(resultant_string)}")
        for char in self.input_string:
            if char not in self.substring:
                resultant_string.append(char)
                print(f"The status of the resultant string --> {resultant_string}")
        output_string = ''.join(resultant_string)
        print(f"The input string before removal --> {self.input_string}")
        print(f"The output string after removal --> {output_string}")

    """ 
    Using the set() method to achieve the same
    """
    def extract_using_set(self):

        resultant_string = ''.join(list(set(self.input_string)- set(self.substring)))
        print(f"The Raw input string before extraction --> {self.input_string}")
        print(f"The output string after extraction --> {resultant_string}")


""" 
create object and function calls 
"""
test_obj = CharacterExtraction()

# calling first way of extracting characters
test_obj.extract_using_loop_way()

# second way to achieve the same
test_obj.extract_using_set()