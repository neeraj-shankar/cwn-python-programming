# Simple Generator function for demontration functionality
def generator_fun():
    
    yield 10
    yield 20
    yield 30

# calling the generator function
for i in  generator_fun():
    print(i)


##############################################################################
## Using Generator Function to get perfect sqaures.
##############################################################################
print(f'--'*50)

def perfect_squares():
    n = 1
    while n <= 10:
        sqaure = n * n
        yield sqaure
        n += 1

# calling the perfect_square()
values = perfect_squares()

for value in values:
    print(value)