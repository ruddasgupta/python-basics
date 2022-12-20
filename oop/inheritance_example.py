# Python code to demonstrate how parent constructors
# are called.

# parent class
import logging


class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.id_number))


# child class
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id_number)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.id_number))
        print("Post: {}".format(self.post))

        logging.debug('This is a debug message')


if __name__ == '__main__':
    # creation of an object variable or an instance
    a = Employee('Roger', 886012, 200000, "Intern")

    # calling a function of the class Person using
    # its instance
    a.display()
    a.details()
