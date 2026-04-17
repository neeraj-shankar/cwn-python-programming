class MyClass:

    def __new__(cls, *args):
        print(f"I am being called.......")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        print(f"Init method being called.....")
        # self.temp = 20
        self.value = value

class UpperString(str):

    def __new__(cls, value):

        print(f"Converts string to capital and then return")
        instance = super().__new__(cls, value.upper())
        return instance

if __name__ == "__main__":

    obj1 = MyClass(20)
    print(f"The value of instance variables: {obj1.value}")
    # print(f"Another instance value: {obj1.temp}")

    obj2 = UpperString("Neeraj")
    print(obj2)


