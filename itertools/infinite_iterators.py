# Python program to demonstrate
# infinite iterators

import itertools

if __name__ == '__main__':
    # for in loop
    for i in itertools.count(5, 5):
        if i == 35:
            break
        else:
            print(i, end=" ")
    print()

    count = 0

    # for in loop
    for i in itertools.cycle('AB'):
        if count > 7:
            break
        else:
            print(i, end=" ")
            count += 1
    print()

    l = ['Hello', 'World', 'Hi']

    # defining iterator
    iterators = itertools.cycle(l)

    # for in loop
    for i in range(6):
        # Using next function
        print(next(iterators), end=" ")
    print()

    # using repeat() to repeatedly print number
    print("Printing the numbers repeatedly : ")
    print(list(itertools.repeat(25, 4)))
