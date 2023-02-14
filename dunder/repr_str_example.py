class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     print('inside str')
    #     return "Person: {}, Age: {}".format(self.name, self.age)

    def __repr__(self):
        print('inside repr')
        return "Person: {}, Age: {}".format(self.name, self.age)


if __name__ == '__main__':
    person = Person('Sarah', 25)
    # print(person.__str__())
    # print(person.__repr__())
    print(person)


