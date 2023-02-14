# Python example to check if a class is
# subclass of another

class Base(object):
    pass  # Empty Class


class Derived(Base):
    pass  # Empty Class


if __name__ == '__main__':
    # Driver Code
    print(issubclass(Derived, Base))
    print(issubclass(Base, Derived))

    d = Derived()
    b = Base()

    # b is not an instance of Derived
    print(isinstance(b, Derived))
    print(isinstance(d, Derived))

    # But d is an instance of Base
    print(isinstance(d, Base))
    print(isinstance(b, Base))
