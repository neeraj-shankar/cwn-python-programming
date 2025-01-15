class NonRepeatingSubstring:

    def __init__(self, input_string):
        self.input_string = input_string

    def solutionBruteforce(self):
        """
        Approach:
        This method iterates through all possible substrings of the input string and determines the length
        of the longest substring without repeating characters.

        Time and Space Complexity:
        TC: O(n^3) and SC: O(1)
        """
        
        n = len(self.input_string) 
        max_sum = 0
        s = 0
        e = 0
        for i in range(0, n):

            for j in range(i, n):
                
                sum = 0
                for k in range(i, j+1):
                    sum += self.input_string[k]

                if sum > max_sum:
                    max_sum = sum
                    s = i
                    e = j

        print(f"Start and End index of max subarray: {s, e}")
        return max_sum


    def solution_sliding_window(self):
        """
        Approach:
        This method uses the sliding window approach to find the length of the longest substring without repeating
        characters more efficiently.

        Time and Space Complexity:
        TC: O(n) and SC: O(n)
        """
        
        n = len(self.input_string) 
        max_sum = 0
        s = 0
        e = 0
        unique_chars = set()

        for i in range(0, n):

            current_char = self.input_string[i]
            while(current_char in unique_chars):
                unique_chars.remove(self.input_string[s])
                s += 1
            
            unique_chars.add(current_char)

            # check and update max sum
            max_sum = max(max_sum, len(unique_chars))
        return max_sum
    
if __name__ == "__main__":

    s = "abcabcbb"

    # create class instance
    nrs = NonRepeatingSubstring(s)

    result = nrs.solution_sliding_window()
    print(f"Max Sum: {result}")
