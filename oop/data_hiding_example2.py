# A Python program to demonstrate that hidden
# members can be accessed outside a class
class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 10


if __name__ == '__main__':
    # Driver code
    myObject = MyClass()
    print(myObject._MyClass__hiddenVariable)
