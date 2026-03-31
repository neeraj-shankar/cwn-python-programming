"""
Problem:
Given a list of sentences, return a dictionary where each key is a word and the value is another 
dictionary containing:
count: total occurrences of the word
sentences: list of sentence indices where the word appears
"""
sentences = [
    "Python is great",
    "I love Python programming",
    "Python is powerful and great"
]
from collections import defaultdict
# Brute force solution
result = {}

for idx, sentence in enumerate(sentences):

    words = sentence.lower().replace(',', '').replace('.', '').split()
    print(words)

    for word in words:

        # Check if the word exists as key in resulut dictionary, if not initialize it
        if word not in result:
            result[word] = {"count": 0, "sentences":[]}

        result[word]['count'] += 1

        # Add the index of the sentence which has the word if that already not present
        if idx not in result[word]['sentences']:
            result[word]['sentences'].append(idx)
print(result)

result2 = defaultdict(lambda: {'count': 0, 'sentences': set()})  # SET instead of list
print(result2)