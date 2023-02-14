import itertools
import operator

if __name__ == '__main__':
    # initializing list 1
    li1 = [1, 4, 5, 7]

    # using accumulate()
    # prints the successive summation of elements
    print("The sum after each iteration is : ", end="")
    print(list(itertools.accumulate(li1)))

    # using accumulate()
    # prints the successive multiplication of elements
    print("The product after each iteration is : ", end="")
    print(list(itertools.accumulate(li1, operator.mul)))

    # using accumulate()
    # prints the successive summation of elements
    print("The sum after each iteration is : ", end="")
    print(list(itertools.accumulate(li1)))

    # using accumulate()
    # prints the successive multiplication of elements
    print("The product after each iteration is : ", end="")
    print(list(itertools.accumulate(li1, operator.mul)))

    li1 = [1, 4, 5, 7]

    # initializing list 2
    li2 = [1, 6, 5, 9]

    # initializing list 3
    li3 = [8, 10, 5, 4]

    # using chain() to print all elements of lists
    print("All values in mentioned chain are : ", end="")
    print(list(itertools.chain(li1, li2, li3)))

    # initializing list 1
    li1 = [1, 4, 5, 7]

    # initializing list 2
    li2 = [1, 6, 5, 9]

    # initializing list 3
    li3 = [8, 10, 5, 4]

    # initializing list of list
    li4 = [li1, li2, li3]

    # using chain.from_iterable() to print all elements of lists
    print("All values in mentioned chain are : ", end="")
    print(list(itertools.chain.from_iterable(li4)))

    # using compress() selectively print data values
    print("The compressed values in string are : ", end="")
    print(list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

    # initializing list
    li = [2, 4, 5, 7, 8]

    # using dropwhile() to start displaying after condition is false
    print("The values after condition returns false : ", end="")
    print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))

    # initializing list
    li = [2, 4, 5, 7, 8]

    # using filterfalse() to print false values
    print("The values that return false to function are : ", end="")
    print(list(itertools.filterfalse(lambda x: x % 2 == 0, li)))

    # initializing list
    li = [2, 4, 5, 7, 8, 10, 20]

    # using islice() to slice the list acc. to need
    # starts printing from 2nd index till 6th skipping 2
    print("The sliced list values are : ", end="")
    print(list(itertools.islice(li, 1, 6, 2)))

    # initializing tuple list
    li = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]

    # using starmap() for selection value acc. to function
    # selects min of all tuple values
    print("The values acc. to function are : ", end="")
    print(list(itertools.starmap(min, li)))

    # initializing list
    li = [2, 4, 6, 7, 8, 10, 20]

    # using takewhile() to print values till condition is false.
    print("The list values till 1st false value are : ", end="")
    print(list(itertools.takewhile(lambda x: x % 2 == 0, li)))

    # initializing list
    li = [2, 4, 6, 7, 8, 10, 20]

    # storing list in iterator
    iti = iter(li)

    # using tee() to make a list of iterators
    # makes list of 3 iterators having same values.
    it = itertools.tee(iti, 3)

    # printing the values of iterators
    print("The iterators are : ")
    for i in range(0, 3):
        print(list(it[i]))

    # using zip_longest() to combine two iterables.
    print("The combined values of iterables is  : ")
    print(*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue='_')))
