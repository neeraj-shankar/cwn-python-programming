""" 
The requirement is to replace occurrence of only duplicate, i.e from second occurrence. This has applications in many
domains.
"""


class DuplicateRemoval:
    # class variable for input string
    input_string = "Avenges is one of the highest grossing movie. Avengers was distributed by Disney. Disney is very " \
                   "big franchise"

    """ 
    Using split() + enumerate() + loop 
    """

    def replace_duplicates(self):
        # first split each word separated by space and store in list
        string_list = self.input_string.split(" ")
        print(f"The substring list after splitting --> {string_list}")
        resultant_string = []
        print(f"The empty set --> {resultant_string} and the type is {type(resultant_string)}")

        # replace the second occurrence and further occurrence of the substring
        replacement_mapping = {"Avengers": "It", "Disney": "It"}
        for index, substring in enumerate(string_list):
            if substring in replacement_mapping:
                print(f"Check for substring in replacement_mapping --> {string_list[index]}")
                if substring in resultant_string:
                    print(f"The string list value for exchange --> {string_list[index]} with replacement list --> {replacement_mapping[substring]}")
                    string_list[index] = replacement_mapping[substring]
                    print(f"The resultant substring list after replacement --> {string_list}")
                else:
                    resultant_string.append(substring)
                    print(f"The status of the resultant string now --> {resultant_string}")
        resultant_string = " ".join(string_list)
        print(f"The string list after modification --> {string_list}")
        print(f"The formatted string is below: \n{resultant_string}")


""" 
create object and call the required function for testing use case
"""


def use_case_separator():
    print(
        "\n============================================================================================================"
    )


test_obj = DuplicateRemoval()

use_case_separator()
test_obj.replace_duplicates()
