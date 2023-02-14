class Employee:
    id = 10
    name = "John"

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))
        # Creating a emp instance of Employee class


if __name__ == '__main__':
    emp = Employee()

    # Deleting the property of object
    # del emp.id
    # Deleting the object itself
    del emp
    emp.display()
