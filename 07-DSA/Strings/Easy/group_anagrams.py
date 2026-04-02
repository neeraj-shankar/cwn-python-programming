"""
Given an array of strings, group the anagrams together. You can return the answer in any order.

Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
"""

class AnagramGroups:

    def solution_hashmap(self, str_list: list[str]):
        """
        1. Iterate through the strings.
        2. Sort each string and use the sorted string as key in hm.
        3. For each key, append the corresponding word in hm.
        3. Iterate through hm and add to the values to ans list
        """

        hm = {}

        for word in str_list:

            key = ''.join(sorted(word))

            if not key in hm:
                hm[key] = list()
            
            hm[key].append(word)
        ans = list(hm.values())
        print(ans)

    def solution_hashmap_optimized(self, word_list: list[str]):

        n = len(word_list)

        hm = {}

        for idx, word in enumerate(word_list):

            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            key = tuple(freq)

            if not key in hm:
                hm[key] = list()
            hm[key].append(word)
        
        return list(hm.values())

if __name__ == "__main__":

    ag = AnagramGroups()
    word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Grouped Anagrams: ", ag.solution_hashmap(word_list))
    print("Grouped Anagrams: ", ag.solution_hashmap_optimized(word_list))

