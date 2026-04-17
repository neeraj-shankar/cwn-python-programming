from abc import ABC, abstractmethod
class Payements(ABC):

    @abstractmethod
    def pay(self, amount: int)-> bool:
        pass 


# Credit Card 
class CreditCardPayement(Payements):

    def pay(self, amount: int)->bool:
        print(f"Amount of {amount} debited from the credit card.")
        print(super().pay(10))
        return True
    
class Paytm(Payements):

    def pay(self, amount: int)-> bool:
        print(f"Successful Transaction of {amount} done using paytm.")
        return True
    
# Testing the two payment types
CreditCardPayement().pay(100)
Paytm().pay(500)

# =======================================================================================
# ==========================  Using the Interface as a Type =============================
# =======================================================================================

class PayementProcessor(ABC):

    @abstractmethod
    def process_payement(self, amount: float)->bool:
        pass


def checkout(processor: PayementProcessor, total: float)-> bool:

    success = processor.process_payement(total)

    if success:
        print(f"Order Completed......")