class Student:
    school_name = 'XYZ School'  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute


if __name__ == '__main__':
    std = Student("Steve", 25)
    print(std.school_name)
    print(std.name)
    print(std.age)
