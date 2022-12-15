class Employee:
    def __new__(cls):
        print("__new__ method is called")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print("__init__ method is called")
        self.name = 'Roger'


if __name__ == '__main__':
    emp = Employee()
