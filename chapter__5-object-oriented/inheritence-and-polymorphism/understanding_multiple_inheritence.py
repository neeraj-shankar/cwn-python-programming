"""
Multiple Inheritance
-----------------------------------------------------------
When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all
the features of the base case.
"""
from format_output import  use_case_separator


class LivingOrganism(object):
    # Initializing the constructor which describes the core property of living organism
    def __init__(self, movement, nutrition, digestion, respiration, growth, excretion, reproduction, sensitivity):
        self.movement = movement
        self.nutrition = nutrition
        self.digestion = digestion
        self.respiration = respiration
        self.growth = growth
        self.excretion = excretion
        self.reproduction = reproduction
        self.sensitivity = sensitivity

    # Function to represent the nutritional requirement of a living organism
    def consume_nutrition(self):
        print(f"The following nutritional consumption required --> {self.nutrition}")


class AnimalLife(LivingOrganism):
    def __init__(self, eukaryotic_cells, heterotrophy, nervous_system, nutrition):
        self.eukaryotic_cells = eukaryotic_cells
        self.heterotrophy = heterotrophy
        self.nervous_system = nervous_system
        self.nutrition = nutrition
        print(f"The property of an animal is based on --> {self.eukaryotic_cells}, {self.heterotrophy} and "
              f"{self.nervous_system}")

    # Function to represent the types of cell animal have
    def cellular_structure(self):
        print(f"Cellular Structure--> {self.eukaryotic_cells}")


class PlantLife(LivingOrganism):

    def __int__(self):
        print(f" I am plant life constructor")


"""
Class objects and function calls
"""
animal_cell_type = "The Animal cells are eukaryotic. Means have a nucleus"
animal_heterotrophy = "Consume food by eating other organism"
animal_nervous_system = "Can be from simple to complex"
animal_nutrition = "Nutrition is key need"

# Creating animal class object which is sub-class of LivingOrganism
animal = AnimalLife(animal_cell_type, animal_heterotrophy, animal_nervous_system, animal_nutrition)
use_case_separator()
animal.cellular_structure()
# calling LivingOrganism function from AnimalLife
animal.consume_nutrition()



