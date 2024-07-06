"""
Find the longest common prefix among an array of strings.
"""


class LogestPrefixString:

    def __init__(self, data) -> None:
        
        self.data = data


    def longest_common_prefix_horizontal(self):
        """
        1. Start with the first string as the initial common prefix. 
        
        2. Iterate through the remaining strings, updating the common prefix to match characters
           from each string until there's no match or the end of any string is reached.
        """
        
        if not self.data:
            return ""
        prefix = self.data[0]
        for string in self.data[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[0:-1]
                print(f"Current Prefix Status: {prefix}")
                if not prefix:
                    return ""
        return prefix
    
    def longest_common_prefix_vertical(self):
        """
        1. Iterate through the characters of the first string.
        2. Compare each character with the corresponding character in the other strings.
        3. Stop when a character doesn't match or the end of any string is reached.
        
        # Time Complexity: O(S), where S is the sum of all characters in all strings
        # Space Complexity: O(1)
        """
        if not self.data:
            return ""
        for i, char in enumerate(self.data[0]):
            for string in self.data[1:]:
                if i >= len(string) or string[i] != char:
                    return self.data[0][:i]
        return self.data[0]
    
    def longest_common_prefix_divide_and_conquer(self):
        """
        1. Divide the array of strings into two halves.
        2. Recursively find the longest common prefix of each half.
        3. Merge the two longest common prefixes.

        # Time Complexity: O(S), where S is the sum of all characters in all strings
        # Space Complexity: O(m*log(n)), where m is the length of the longest prefix and n is the number of strings
        """
        if not self.data:
            return ""
        return self._divide_and_conquer(self.data)

    def _divide_and_conquer(self, strings):
        if len(self.data) == 1:
            return self.data[0]
        mid = len(self.data) // 2
        left_prefix = self._divide_and_conquer(self.data[:mid])
        right_prefix = self._divide_and_conquer(self.data[mid:])
        return self._merge(left_prefix, right_prefix)

    def _merge(left_prefix, right_prefix):
        min_len = min(len(left_prefix), len(right_prefix))
        for i in range(min_len):
            if left_prefix[i] != right_prefix[i]:
                return left_prefix[:i]
        return left_prefix[:min_len]

    
    def longest_common_prefix_binary_search(self, strings):
        if not strings:
            return ""
        min_len = min(len(s) for s in strings)
        low, high = 0, min_len
        while low < high:
            mid = (low + high + 1) // 2
            if self._is_common_prefix(strings, mid):
                low = mid
            else:
                high = mid - 1
        return strings[0][:low]

    def _is_common_prefix(strings, length):
        prefix = strings[0][:length]
        return all(s.startswith(prefix) for s in strings)

    # Time Complexity: O(S*log(n)), where S is the sum of all characters in all strings and n is the number of strings
    # Space Complexity: O(1)


    def longest_common_prefix_sort(self):
        """
        1. Sort the array of strings.
        2. Compare the first and last strings to find the longest common prefix.

        # Time Complexity: O(n*log(n) + S), where n is the number of strings and S is the sum of all characters in all strings
        # Space Complexity: O(1)
        """
        if not self.data:
            return ""
        self.data.sort()
        first, last = self.data[0], self.data[-1]
        for i, char in enumerate(first):
            if char != last[i]:
                return first[:i]
        return first











if __name__ == "__main__":
    
    raw_data = ["flower", "flow", "flight"]

    logestPrefixString = LogestPrefixString(raw_data)

    result = logestPrefixString.longest_common_prefix_horizontal()
    print(f"The longest common prefix is: {result}")

    result = logestPrefixString.longest_common_prefix_vertical()
    print(f"The longest common prefix is: {result}")

    
    result = logestPrefixString.longest_common_prefix_sort()
    print(f"The longest common prefix is: {result}")