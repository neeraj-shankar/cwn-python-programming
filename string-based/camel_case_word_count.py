##############################################################################
## Probem Statement: There is a sequence of words in CamelCase as a string of
## letters, s, having the following properties:
## 1. It is a concatenation of one or more words consisting of English letters.
## 2. All letters in the first word are lowercase.
## 3. For each of the subsequent words, the first letter is uppercase and rest
## of the letters are lowercase.
##############################################################################

import re


def word_count_using_regex(sentence):
    total_words = 1
    re_expression = r"[A-Z][a-z]*"
    total_words = len(re.findall(re_expression, sentence)) + 1
    print(re.findall(re_expression, sentence))
    print(f"Word Count: {total_words}")


##############################################################################

# input data
input_data = "camelCaseWordExample"
word_count_using_regex(input_data)


##############################################################################
## Second Way --> using for loop
##############################################################################
def word_count_using_loop(sentence):
    total_words = 1
    for word in sentence:
        if word.isupper():
            total_words += 1

    print(f"Total words: {total_words}")


##############################################################################
# making function call
input_data = "camelCaseWord"
word_count_using_loop(input_data)
