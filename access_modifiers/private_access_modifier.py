# program to illustrate private access modifier in a class

class Student:
    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __display_details(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def access_private_function(self):
        # accessing private member function
        self.__display_details()


if __name__ == '__main__':
    # creating object
    obj = Student("Bob", 1706256, "Computer Science")

    # calling public member function of the class
    obj.access_private_function()
