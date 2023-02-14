# A Python program to demonstrate use of
# generator object with next()

# A generator function
def simple_enerator():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    # x is a generator object
    x = simple_enerator()

    # Iterating over the generator object using next
    print(next(x))  # In Python 3, __next__()
    print(next(x))
    print(next(x))
