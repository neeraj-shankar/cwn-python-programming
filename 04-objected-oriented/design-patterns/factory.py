from abc import ABC, abstractmethod

"""
===================================================================================================
The Factory Pattern is a creational design pattern that provides an interface for creating objects 
without specifying the exact class of object that will be created. 

It delegates the instantiation logic to subclasses or a separate factory method.
"""
# Transport Interface
class Transport(ABC):

    @abstractmethod
    def deliver(self):
        pass


# Concrete implementation
class Truck(Transport):

    def deliver(self):
        print(f"Delivering by the road.")

class Ship(Transport):

    def deliver(self):
        print("Delivering by the sea route.")

        return 1

class Logistics(ABC):

    @abstractmethod
    def create_transport(self)-> Transport:
        """The actual Factory Method"""
        pass 

    def plan_delivery(self):
        # The factory method is used here to get a product
        transport = self.create_transport()

        return f"Logistics: {transport.deliver()}"
    
# Concreate creators
class RoadLogistics(Logistics):
    def create_transport(self)-> Transport:
        return Truck()
    
class SeaLogistics(Logistics):
    def create_transport(self)-> Transport:
        return Ship() 
    
# Testing 
def client(logistics: Logistics):
    print(logistics.plan_delivery())

app_mode = "sea"

if app_mode == "sea":
    client(SeaLogistics())
else: 
    client(RoadLogistics())