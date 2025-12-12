
# Basic Generator

def i_am_gen():
    print("Start.........")
    x = yield 10
    print(f"Got: {x}",)
    yield 2
    yield 3

import types
from typing import Generator

g = i_am_gen()

print(isinstance(g, types.GeneratorType)) # True
print(isinstance(g, Generator)) # True

print(next(g))
print(g.send(29))
print(next(g))

# Create a generator with or without return statement
def gen():
    yield 11
    yield 22
    return 99

g1 = gen()
print(next(g1))
print(next(g1))
# print(next(g1))

# Generator behavior when close() is called

def mygen():
    try:
        yield 20

    except GeneratorExit:
        pass
        # yield 30 # Raises runtime error
    finally:
        print(f"Generator is getting closed")

g = mygen()
print(next(g))