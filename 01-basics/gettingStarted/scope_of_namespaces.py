x = "I am Global"

def my_function():
    y = "I am Local"
    print("--- LOCALS INSIDE FUNCTION ---")
    print(locals())
    print("\n--- GLOBALS INSIDE FUNCTION ---")
    # This will still show the huge dictionary with '__name__', 'x', etc.
    print(globals()) 

my_function()

print("\n--- LOCALS AT TOP LEVEL ---")
print(locals()) # This will match globals() again