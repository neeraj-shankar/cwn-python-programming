class ConditionalStatementProblem:

    def __init__(self) -> None:

        pass

    @staticmethod
    def find_integer_type():
        """
        Asks the user for a number and prints whether the number is positive, negative, or zero.
        """

        # Takes input from user, typecast it to integer and store as varibale
        try:
            input_number = int(input(f"Please enter to check the type of integer: "))

            if input_number > 0:
                print(f"The given number: {input_number} is a positive integer number.")

            elif input_number < 0:
                print(f"The given number: {input_number} is a negative integer number.")

            else:
                print(f"The given number: {input_number} is a 0 number.")

        except ValueError as ex:
            print(f"The provided input is not a valid integer. ERROR: {ex}")

    @staticmethod
    def find_life_stage_status():
        """
        Takes an age as input and prints the life stage of a person (child, teenager, adult, senior) based on that age.
        """
        try:
            age = int(input(f"Please enter your age: "))

            assert age > 0, "Age cannot be negative. Provide positive integer."

            if age < 14:
                print(f"You are a child with age: {age}")
            elif age >= 14 and age < 18:
                print(f"You are a teenager with age: {age}")

            elif age >= 18 and age < 41:
                print(f"You are an adult with age: {age}")
            else:
                print(f"You are a senior citizen with age: {age}")

        except ValueError as ex:
            print(f"Age should be integer number. ERROR: {ex}")

    @staticmethod
    def find_larger_number():
        """
        Reads two numbers and prints the larger one. If the numbers are equal, print a message stating that they are equal.
        """
        try:
            first_number = int(input(f"Please enter the first number: "))
            second_number = int(input(f"Please enter second number: "))

            if first_number > second_number:
                print(
                    f"The  first number: {first_number} is greater than second number: {second_number}"
                )
            elif second_number > first_number:
                print(
                    f"The  Second number: {second_number} is greater than first number: {first_number}"
                )
            else:
                print(
                    f"The  first number: {first_number} and second number: {second_number}. Both are equal"
                )

        except ValueError as ex:
            print(f"Age should be integer number. ERROR: {ex}")

    @staticmethod
    def determine_alphabet_type():
        """
        A program that takes a letter as input and determines whether it is a vowel or a consonant.
        If the input is not a letter, print an appropriate error message.
        """
        given_alphabet = input(f"Please enter a letter to chec its type: ")

        assert (
            len(given_alphabet) == 1
        ), "There are more than one characters. Please provide only single character."


    @staticmethod
    def determine_even_odd_number():
        """
        Takes an integer number and tell the user if given number is odd or even
        """
        try:

            input_number = int(
                input(f"Please enter any number to determine if its even or odd: ")
            )

            if input_number % 2 == 0:
                print(f"The given {input_number} is an even number.")
            elif input_number == 0:
                print(
                    f"The given number is {input_number} which is neither odd nor even"
                )
            else:
                print(f" The given number: {input_number} is an odd number")

        except ValueError as ex:
            print(f"The number should be an Integer. ERROR: {ex}")


    @staticmethod
    def determine_leap_year():
        """
        Takes an integer number and tell the user if given number is odd or even
        A leap year the one that satisfy the following condition:
        1. It should be divible by 4
        2. It should no be divible 100 
        3. If it it divisible 100, it should be not divisible 400 as well
        """
        try:

            year = int(
                input(f"Please enter a year: ")
            )

            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("Leap Year")
                    else:
                        print("Not Leap Year")
                else:
                    print("Leap Year")

            else:
                print(f"Not Leap year")

        except ValueError as ex:
            print(f"The number should be an Integer. ERROR: {ex}")

    @staticmethod
    def is_leap_year():
        """
        Determine whether a given year is a leap year. To summarize, the rules for a leap year are:

        1. If the year is not divisible by 4, it is a common year (not a leap year).
        2. If the year is divisible by 4 but not by 100, it is a leap year.
        3. If the year is divisible by both 100 and 400, it is a leap year.
        4. If the year is divisible by 100 but not by 400, it is a common year.

        :return: True if the year is a leap year, False otherwise
        """
        # Check if the year is divisible by 4 but not by 100,
        # or if the year is divisible by 400.
        year = int(input("Enter a year to check: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False


if __name__ == "__main__":

    testConditionalStatement = ConditionalStatementProblem()

    # testConditionalStatement.find_integer_type()
    # testConditionalStatement.find_life_stage_status()
    # testConditionalStatement.find_larger_number()
    # testConditionalStatement.determine_alphabet_type()
    # testConditionalStatement.determine_even_odd_number()
    testConditionalStatement.determine_leap_year()
