""" 
Here, we will be going through multiple question based on list comprehension
"""


class BasicListComprehensionQuestion:
    animal_list = ["Jaguar", "Humans", "Jellyfish", "Beetles"]
    phylum_list = ["Chordata", "Chordata", "Cnidaria", "Arthropod"]

    def digit_sum(self, custom_list):
        total_sum = 0
        for item in str(custom_list):
            total_sum += int(item)
        return total_sum

    # ==================Creates a list by finding digit sum of every odd element in the list ============
    def finding_sum_of_digits(self, custom_list):
        list_digit_sum = [self.digit_sum(i) for i in custom_list if i & 1]
        return list_digit_sum

    # ============ Coverts two list into list of two tuples =============================================
    def convert_to_list_to_tuples(self):
        animal_phylum_list = [
            (animal, phylum)
            for animal, phylum in zip(self.animal_list, self.phylum_list)
        ]
        return animal_phylum_list

    def reverse_each_string(self):
        reversed_animal_string_list = [
            new_string[::-1] for new_string in self.animal_list
        ]
        return reversed_animal_string_list


""" 
Objects and functions calls handing
"""


def formatting():
    return print(
        "========================================================================"
    )


basic_qa = BasicListComprehensionQuestion()

# calling the finding to calculate the sum of digits of a list for order numbers
num_list = [1, 2, 3, 4, 5, 6, 7]
sum_of_digits = basic_qa.finding_sum_of_digits(num_list)
print(f"The sum of the odd digits are as follows: {sum_of_digits}")
formatting()

# ===========================calling function to combine two list into one list of two tuples============
list_of_tuples = basic_qa.convert_to_list_to_tuples()
print(
    f"The list by combing two tuples to show animal and its phyllum --> {list_of_tuples}"
)


# ===========================Reverse Each string in a list =============================================
formatting()
reverse_list = basic_qa.reverse_each_string()
print(f"Reversed string of animals -- {reverse_list}")
