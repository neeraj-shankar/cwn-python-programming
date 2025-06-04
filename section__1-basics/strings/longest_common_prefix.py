class LongestCommonPrefix:

    def _init__(self, input_string):
        self.string = input_string

    def solution_horizontal_scan(self):
        """
        Key Idea:

        """

        # assume first string to be common prefix
        common_prefix = self.string[0]

        for word in self.string[1:]:

            while not word.startswith(common_prefix):
                common_prefix = common_prefix[:-1]
        
        return common_prefix;

if __name__ == "__main__":

    raw = ["flower", "flow", "flight"]

    # LongestCommonPrefix Class instance
    lcf = LongestCommonPrefix(raw)

    print(f"The longest common prefix: {lcf.solution_horizontal_scan()}")

