"""
Due to the fact that not all the containers in Python are mutable, such as string, the sort function doesn’t work as
it inplace tries to sort and immutability stops this. Let’s discuss certain ways in which a string can be sorted in a
reverse way.
"""
from format_output import use_case_separator
from functools import reduce


class StringReverseSorting:
    """
    Using sorted(), reverse and join
    """
    @staticmethod
    def using_sorted_reverse_join(custom_string):

        # sorted() sort the character in descending way make a list of sorted characters
        sorted_string = sorted(custom_string, reverse=True)

        # join() taking all characters from list and form a string by joining them
        result = ''.join(sorted_string)
        print(f"The sorted string letters --> {result}")

    @staticmethod
    def using_sorted_reverse_reduce(custom_string):

        # reduce() takes x as the first element of the list and keep adding all element one by one
        result = reduce(lambda x, y: x + y, sorted(custom_string, reverse=True))
        print(f"The reverse sorted letters using reduce --> {result}")

    @staticmethod
    def using_list_sort_join(custom_string):
        string_list = list(custom_string)
        print(f"The list of characters --> {string_list}")
        # sort() method sorts all the letters of the list in given order
        string_list.sort(reverse=True)
        # join() taking all characters from list and form a string by joining them
        result = ''.join(string_list)
        print(f"The reverse sorted letters using list --> {result}")


"""
Method call and input data
"""
input_string = "neeraj shankar"

use_case_separator()
StringReverseSorting.using_sorted_reverse_join(input_string)
use_case_separator()
StringReverseSorting.using_sorted_reverse_reduce(input_string)
use_case_separator()
StringReverseSorting.using_list_sort_join(input_string)


