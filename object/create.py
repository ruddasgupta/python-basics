class Employee:
    id = 10
    name = "John"

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


if __name__ == '__main__':
    # Creating a emp instance of Employee class
    emp = Employee()
    emp.display()
