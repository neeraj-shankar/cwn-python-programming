"""
Demonstration of basic inheritence working and properties
"""

class Animal:
    def __init__(self):
        self.number_of_eyes = 2

    def breathe(self):
        print('Inhale and Exhale')

class Fish(Animal):
    """
    Fish Class Inheriting the Animal Class
    """
    def swim(self):
        print('Swimming into the sea')         


"""
Creating objects and calling methods
"""
fish_obj = Fish()
fish_obj.swim()
print(fish_obj.number_of_eyes)
fish_obj.breathe()
