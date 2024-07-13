class MyClass:
    def __init__(self):
        self.__private_var = "I am private"


    def getter_test(self):

        return self.__private_var

# Outside the class
instance = MyClass()
# Accessing the mangled name
# print(instance._MyClass__private_var)  # Outputs: I am private

output = instance.getter_test()
print(output)