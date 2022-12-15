class Person:
    # class attribute
    attr1 = "person"

    # Instance attribute
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # Driver code
    # Object instantiation
    Rodger = Person("Rodger")
    Tommy = Person("Tommy")

    # Accessing class attributes
    print("Rodger is a {}".format(Rodger.__class__.attr1))
    print("Tommy is also a {}".format(Tommy.__class__.attr1))

    # Accessing instance attributes
    print("My name is {}".format(Rodger.name))
    print("My name is {}".format(Tommy.name))
