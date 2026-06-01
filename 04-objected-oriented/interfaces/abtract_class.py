
"""
===================================================================================================
Abract Class and abstract Methods

abtractmethod
-----------------------------------------------------------------------------------------
An abstract method is a method declared in the abstract class but contains no implementation 
(usually just a pass statement). Any "concrete" child class must override this method, or 
Python will refuse to let you create an instance of that child.
-----------------------------------------------------------------------------------------

===================================================================================================
"""

from abc import ABC, abstractmethod

class DocumentConvertor(ABC):

    @abstractmethod
    def load_file(self, path):
        """Must be implemented to load the specific file type"""
        pass 
    
    @abstractmethod
    def convert_to_pdf(self):
        """Must be implemented to perform the conversion"""
        pass

    def common_utility(self):
        # Concrete methods CAN exist in abstract classes
        print("Performing standard pre-conversion checks...")


class ExcelConvetor(DocumentConvertor):

    def load_file(self, path):
        pass
    
    def convert_to_pdf(self):
        pass

obj = ExcelConvetor()
print(obj)