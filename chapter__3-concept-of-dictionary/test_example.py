""" 
Python program for question asked in python quiz
"""

class PracticeSet:

    """ 
    Changing the initial state of a dictionary
    """
    def change_state(self):
        initial_dictionary = {
            "one": 1,
            "two": 2,
        }

        # final_dictionary = {
        #     "one": 1,
        #     "two": 2,
        #     "three": 3,
        # }

        # Option one
        initial_dictionary['three'] = 3
        final_dictionary = initial_dictionary
        print(final_dictionary)

        # option two
        try:
            final_dict_2 = initial_dictionary.append(3)
        except AttributeError as e:
            print(f"The append method is not supportted in dictionary ---{e}")

        # option three
        # final_dict_3 = initial_dictionary += {"three": 3}

        # option 4
        final_dict_4 = initial_dictionary["four"] = 4
        print(final_dict_4)
        print(initial_dictionary)

    def line_with_error(self):
        custom_dict = {
            "one": 1,
            "two": 2,
            "three": 3,
        }

        # option 1 
        custom_dict["three"] = [4, 5, 6]
        print(custom_dict)

        #option 2 
        try: 
            for key in custom_dict:
                custom_dict[key] += 2
                # print[custom_dict[key]]
        except TypeError as e:
            print(f"You cannot add int to a string as key -- {e}")    

        #option 3
        try: 
            print(custom_dict[2])
        except KeyError as e:
            print(f"There is no key found --> {e}")



"""     
Object Creation and function calss
"""

sol = PracticeSet()
# result = sol.change_state()
sol.line_with_error()