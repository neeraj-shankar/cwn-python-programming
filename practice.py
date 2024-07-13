
class ParentClass:

    # class variable 
    class_variable = "This a class variable shared acrross all instance of a class."

    __private_variable = "I am private variable"

    def __init__(self, instance_variable):

        self.instance_variable = instance_variable
        self.__private = "Iam private"

    def instance_method(self):

        print("I am instance method and I can aceess instance variables")
        print(f"{self.instance_variable} ACCESSED FROM INSTANCE METHOD")

    def class_method(cls):
        pass
        

if __name__ == "__main__":

    inst1 = ParentClass("I am instance varibale and unique for each instance of the class")

    # accessing class variable
    value = inst1.class_variable
    print(value)

    # accessing private variable directly (not recommended)
    print(inst1._ParentClass.__private)


