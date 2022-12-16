class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = last + "." + first + "@email.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}.{}@email.com'.format(self.last, self.first)


emp1 = Employee('John', 'Smith')

emp1.first = 'Jim'

print(emp1.first)
print(emp1.email())
print(emp1.fullname())
