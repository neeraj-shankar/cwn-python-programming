"""
You are given a sentence represented as an array A of strings, where each string contains only 
lowercase English alphabets.

Your task is to check whether the sentence is a pangram or not.

A pangram is a sentence in which every letter of the lowercase English alphabet (a to z) 
appears at least once.
"""

class PanagramCheck:

    def solution(self, A):
        """
        Algo
        -----------------------------------------
        1. Create a frequency array.
        2. Ierate over each word of given sentence, extract it character and update its pos in the array.
        """

        freq = [0 for _ in range(26)]

        for word in A:

            for char in word:
                # print(f"Order of {char} is {ord(char)} and index {ord(char)- ord('a')} in frequency.")
                freq[ord(char) - ord('a')] += 1

        print(freq)

        for f in freq:

            if f == 0:
                return False
        
        return True

if __name__ == "__main__":

    pc = PanagramCheck()

    # Test Case 1: 
    A = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    print(f"Whether the given sentence Panagram: ", pc.solution(A))

    # Test Case 2: 
    A = ["bit", "scale"]
    print(f"Whether the given sentence Panagram: ", pc.solution(A))

