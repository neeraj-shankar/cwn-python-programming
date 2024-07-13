

class Mammals:

    # Class variables. They are shared among all instance of the class
    kingdom = "Animalia"
    phylum = "Chordata"

    def __init__(self, mammary_gland, neocortex) -> None:

        # Instance variable. They are unique to each instance of the class
        self.mammary_gland = mammary_gland
        self.neocortex = neocortex

    def respire(self):

        print(f"The mammals respire through lungs.")

    def eating_type(self):

        print(f"Mammals can be a Carnivore, Herbivore or Ominvore")
    
    
class Lion(Mammals):

    
    # Overrinding eating_type() to specifically referring to lions
    def eating_type(self):
        print(f"Lions are top predator and carnivore in eating type.")
        


if __name__ == "__main__":

    mammary_gland = "They have mammary glands that help them produce milk to feed their younger ones"
    neocortex = "Presence of region of the brain known as Neocortex"

    lion1_instance = Lion(mammary_gland, neocortex)

    lion1_instance.respire()
    lion1_instance.eating_type()