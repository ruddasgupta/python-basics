def greet1(name1, name2, name3):
    print('Hello ', name1, ' , ', name2, ', and ', name3)


def greet2(*names):
    print('Hello ', names[0], ' , ', names[1], ', and ', names[2])


if __name__ == '__main__':
    greet1('Steve', 'Bill', 'Roger')
    greet2('Steve', 'Bill', 'Roger')  # calling function with string argument
