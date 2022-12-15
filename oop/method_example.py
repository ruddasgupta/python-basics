class Person:
    # class attribute
    attr1 = "person"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is ", self.name)


if __name__ == '__main__':
    # Driver code
    # Object instantiation
    Rodger = Person("Rodger")
    Tommy = Person("Tommy")

    Rodger.speak()
    Tommy.speak()