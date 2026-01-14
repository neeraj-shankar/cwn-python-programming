# Remove Duplicates from a list

def remove_duplicates(numbers):
    
    # Hashset to check the existence of duplicates
    seen = set()
    ans = []

    for num in numbers:

        # If the number is not already there in set, its unique
        if num not in seen:
            ans.append(num)
        seen.add(num)

    return ans 

# The list after duplicates removal
numbers = [1, 2, 3, 3, 2, 5]
print(remove_duplicates(numbers)) # [1, 2, 3, 5]

seen = set()
unique_nums = [x for x in numbers if not (x in seen or seen.add(x))]
print(unique_nums)


def remove_duplicates_inplace(numbers):

    seen = set()
class DuplicatesRemoval:

    def __init__(self, numbers):
        self.numbers = numbers

    def solution_inplace(self):

        seen = set()

        i = 0
        while(i < len(self.numbers)):
            if self.numbers[i] in seen:
                self.numbers.pop(i)
            else:
                seen.add(self.numbers[i])

