class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter  # property-name.deleter decorator
    def name(self, value):
        print('Deleting..')
        del self.__name


if __name__ == '__main__':
    s = Student('Steve')
    print(s.name)
    s.name = 'Bill'
    print(s.name)
