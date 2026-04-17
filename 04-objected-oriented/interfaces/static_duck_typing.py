from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> None:
        ...

class Bird:  # Note: No (Flyer) inheritance here!
    def fly(self) -> None:
        print("Flap flap")

def lift_off(entity: Flyer):
    entity.fly()

# This works because Bird "looks like" a Flyer
lift_off(Bird())