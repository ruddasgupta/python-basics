class Student:
    name = 'unknown'  # class attribute

    def __init__(self):
        self.age = 20  # instance attribute

    @staticmethod
    def tostring():
        print('Student Class')

    # @staticmethod
    # def tostring():
    #     print('name=', name, 'age=', self.age)


if __name__ == '__main__':
    Student.tostring()
