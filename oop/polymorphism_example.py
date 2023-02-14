class Employee:

    def intro(self):
        print("I am an employee")

    def designation(self):
        print("emp-designation")


class Manager(Employee):

    def intro(self):
        print("I am an manager")

    def designation(self):
        print("mang-designation")


class Developer(Employee):

    def intro(self):
        print("I am an developer")

    def designation(self):
        print("dev-designation")


if __name__ == '__main__':
    obj_Employee = Employee()
    obj_spr = Manager()
    obj_ost = Developer()

    obj_Employee.intro()
    obj_Employee.designation()

    obj_spr.intro()
    obj_spr.designation()

    obj_ost.intro()
    obj_ost.designation()
