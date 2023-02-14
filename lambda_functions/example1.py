if __name__ == '__main__':
    square = lambda x: x * x
    print(square(2))
    print((lambda x: x * x)(5))

    greet = lambda name: print('Hello ', name)
    greet('Steve')

    sum = lambda x, y, z: x + y + z
    print(sum(5, 10, 15))

    sqrList = map(lambda x: x * x, [1, 2, 3, 4])
    print(list(sqrList))


def do_something(fn):
    print('Calling function argument:')
    fn()


do_something(lambda: print('Hello World!'))
