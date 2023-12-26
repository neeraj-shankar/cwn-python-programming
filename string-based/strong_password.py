"""
This python program take input from user and validate if the password is strong enough on the following basis:

1. Its length is at least 6.
2. It contains at least one digit.
3. It contains at least one lowercase English character.
4. It contains at least one uppercase English character.
5. It contains at least one special character. The special characters are: !@#$%^&*()-+
"""


class StrongPasswordValidator:

    @staticmethod
    def validate_strong_password(n, password):

        character_count = {
            "special_char": 0,
            "digit_char": 0,
            "capital_char": 0,
            "small_char": 0,
        }

        required_char_count = 6 - len(password)
        missing_char_count = 0
        for char in password:
            print(f"The char in iteration --> {char}")
            if char.isdigit():
                character_count["digit_char"] += 1
            elif char.isupper():
                character_count["capital_char"] += 1

            elif not char.isalpha():
                character_count["special_char"] += 1

            elif char.islower():
                character_count["small_char"] += 1

        for val in character_count.values():
            if val == 0:
                print(f"the item value --> {val}")
                print(f"Missing char count  --> {missing_char_count}")
                missing_char_count += 1

        print(f"the required count --> {required_char_count}")
        print(f"The missing char count --> {missing_char_count}")
        print(f"the dictionary data--> {character_count}")
        return required_char_count if required_char_count > missing_char_count else missing_char_count


"""
"""
fptr = open("output_file.txt", 'w')

num = int(input().strip())

input_password = input()

answer = StrongPasswordValidator.validate_strong_password(num, input_password)

fptr.write(str(answer) + '\n')

fptr.close()
