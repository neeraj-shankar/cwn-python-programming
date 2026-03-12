
class StrictNamingMeta(type):
    """
    Encorcing that the class name should always starts with upper case
    """
    def __new__(cls, name, bases, dct):

        if not name[0].isupper():
            raise TypeError(f"Class name '{name}' must start with an uppercase letter! Be better.")
        
        return super().__new__(cls, name, bases, dct)
    
class UpperCaseAttributeMeta(type):
    """
    Converts the attributes of the class to be in upper case only.
    """

    def __new__(cls, name, bases, dct):
        print(dct)
        # We intercept the class creation and force all attributes to uppercase
        uppercase_attrs = {k.upper(): v for k, v in dct.items() if not k.startswith('__')}
        return super().__new__(cls, name, bases, uppercase_attrs)
    
