class Parent(object):
    def _protected(self):
        print('Base protected')

    def __private(self):
        print('Base private')

    def public(self):
        print('Base public')


class Child(Parent):
    def m1(self):
        self._protected()  # This works

    def m2(self):
        self.__private()

    def m3(self):
        self.public()


if __name__ == '__main__':
    child = Child()
    child.m1()
    # child.m2()
    child.m3()
