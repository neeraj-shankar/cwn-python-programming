"""
There is a collection of rocks where each rock has various minerals embeded in it. 
Each type of mineral is designated by a lowercase letter in the range ascii[a-z]. 

There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs 
at least once in each of the rocks in the collection.

Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.
"""


class Gemstones:
    """
    This class represents a collection of gemstones and provides methods to count the
    unique gemstones present in the collection.
    """

    def __init__(self, collection):
        """
        Initializes a Gemstones object with a collection of gemstone names.

        Args:
            collection (list): A list of strings representing gemstone names. Each string
                may contain duplicate characters.
        """
        self.collection = collection

    def gems_count_using_set(self):
        """
        Counts the number of unique gemstones using sets.

        This method efficiently counts the unique gemstones by converting each gemstone name
        (string) into a set of unique characters and then finding the intersection of all sets.

        Returns:
            int: The number of unique gemstones present in the collection.
        """

        # Convert each string to a set of unique characters
        sets_collection = [set(mineral) for mineral in self.collection]
        print(sets_collection)  # [{'b', 'a', 'c'}, {'b', 'a', 'c'}, {'b', 'c'}]

        # Find the intersection of all sets
        gemstones_set = set.intersection(*sets_collection)
        print(gemstones_set)  # {'b', 'c'}

        return len(gemstones_set)


def gems_count_using_naive_approach(arr) -> int:
    """
    Count the number of gems that occur in all strings of the input array using a naive approach.

    This function iterates through each character of the first string in the input array
    and checks if that character is present in all other strings. If the character is present
    in all strings, it is counted as a gem.

    Args:
        arr (List[str]): The input array of strings.

    Returns:
        int: The total number of gems found in all strings.

    Example:
        >>> gems_count_using_naive_approach(["abc", "def", "ghi"])
        0
        >>> gems_count_using_naive_approach(["abc", "bcd", "cde"])
        1
    """
    total_gems = 0
    for _chr in arr[0]:
        result = all(_chr in item for item in arr)
        if result:
            total_gems += 1
    return total_gems


if __name__ == "__main__":
    rocks_collection = ["abc", "abc", "bc"]

    Gemstones(rocks_collection).gems_count_using_set()
    # {'b', 'c'}
