class Student:
    name = 'unknown'  # class attribute

    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=', cls.name)

    # # Cannot the instance attributes.
    # @classmethod
    # def tostring(cls):
    #     print('Student Class Attributes: name=', cls.name, ', age=', cls.age)


if __name__ == '__main__':
    Student.tostring()
    std = Student()
    std.tostring()
    Student().tostring()
