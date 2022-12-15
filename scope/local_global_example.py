name = 'Steve'


def greet1():
    name = 'Bill'
    print('Hello ', name)


def greet2():
    global name
    name = 'Bill'
    print('Hello ', name)


def greet3():
    globals()['name'] = 'James'
    name = 'Steve'
    print('Hello ', name)


if __name__ == '__main__':
    print(name)
    greet1()
    print(name)
    greet2()
    print(name)
    greet3()
    print(name)
