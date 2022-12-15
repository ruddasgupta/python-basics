class Student:
    __school_name = 'XYZ School'  # class attribute

    def __init__(self, name, age):
        self.__name = name  # instance attribute
        self.__age = age  # instance attribute

    def __show(self):  # private method
        print('This is private method.')


if __name__ == '__main__':
    std = Student("Steve", 25)
    std.__show()
    std.__school_name
    std.__name
    std.__age
