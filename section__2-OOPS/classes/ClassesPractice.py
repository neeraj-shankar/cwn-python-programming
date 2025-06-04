
class ClassesPractice:

    # a class variable
    counter = 0

    # constructor method
    def __init__(self, name):
        self.name = name;
        ClassesPractice.counter += 1

    def __new__(cls, *args, **kwargs):
        print(f"Creating object with __new__")
        instance = super().__new__(cls)
        return instance

    def greet(self):
        print(f"Good Morning {self.name}\n")

if __name__ == "__main__":

    # Create a class instance/object
    obj = ClassesPractice("Neeraj")
    print(isinstance(obj, ClassesPractice))

    obj2 = ClassesPractice("Asati")
    obj3 = ClassesPractice("Rajbhaan")

    obj.greet()

    print(f"Total Instance Created: {ClassesPractice.counter}")
    print(obj.counter)