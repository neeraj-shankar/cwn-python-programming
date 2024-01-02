import random

# word_list = ["advark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# guess = input("Guess a letter: ").lower()

# # Create a empty list of size of chosen word 
# display = []
# end_of_game = False
# while not end_of_game:
#     for letter in chosen_word:
#         if letter == guess :
#             print("Right")
#             display.append(letter)
#         else: 
#             print("Wrong")
#             display.append("_")


#     if "_" not in display:
#         end_of_game = True

# print(display)

word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input