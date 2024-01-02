"""
Python program to demonstrate the diamond problem in multiple inherit
"""


class LandAnimal(object):
    def __int__(self):
        print(f"I am LandAnimal Class Constructor")

    def breathe(self):
        print(f"I live on land and can breathe")


class WaterAnimal(object):
    def __int__(self):
        print(f"I am LandAnimal Class Constructor")

    def breathe(self):
        print(f"I live in water and can breathe")


class AmphibianAnimal(LandAnimal, WaterAnimal):

    def __int__(self):
        print(f"I am amphibian from AmphibianAnimal Class")


"""
Create object and calling the functions
"""
test_obj = AmphibianAnimal()
test_w = WaterAnimal()

