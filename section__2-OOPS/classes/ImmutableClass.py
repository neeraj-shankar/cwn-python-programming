'''
Since immutable objects can’t be changed after they’re created, you have to use __new__ 
if you want to customize them 
'''

class ImmutableString(str):

    def __new__(cls, content):
        print(f"Executing the __new__ method block")

        # Capitalize the string before creation
        content = content.upper()

        return super().__new__(cls, content)

    def __init__(self, content):

        print("Inside __init__")
        # We can't modify self here because str is immutable
        # So this method is mostly useless for str subclasses

if __name__ == "__main__":

    obj = ImmutableString("Hello World")
    print(obj)
