
class LongestCommonPrefix:

    def __init__(self):
        pass

    def solution_vertical_scan(self, in_string: list):

        # Base Case: When empty list of string is given
        if len(in_string) == 0:
            return ""
        
        # Base Case: When list contain only one item
        if len(in_string) == 1:
            return in_string[0]
        
        # Generic Case
        for i in range(0, len(in_string[0])):

            pivot_char = in_string[0][i]

            for j in range(1, len(in_string)):

                curr_char = in_string[j][i]

                if(j <= i and curr_char != pivot_char):
                    return in_string[0][0:i]
                
        return in_string[0]
    
if __name__ == "__main__":

    str_list = ["flow", "flight", "flower"]

    lcp = LongestCommonPrefix()
    ans = lcp.solution_vertical_scan(str_list)
    print(f"Longest Common Prefix: {ans}")