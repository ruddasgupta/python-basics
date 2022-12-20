import math

if __name__ == '__main__':

    # Old vs New
    print('The value of pi is approximately %5.3f.' % math.pi)
    print(f'The value of pi is approximately {math.pi:.3f}.')

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

    for name, phone in table.items():
        print(f'{name:10} ==> {phone:10}')

    animals = 'eels'
    print(f'My hovercraft is full of {animals}.')
    print(f'My hovercraft is full of {animals!r}.')

    bugs = 'roaches'
    count = 13
    area = 'living room'
    print(f'Debugging {bugs=} {count=} {area=}')

    # String Format

    print('We are the {} who say "{}!"'.format('knights', 'Ni'))

    print('{0} and {1}'.format('spam', 'eggs'))
    print('{1} and {0}'.format('spam', 'eggs'))

    print('This {food} is {adjective}.'.format(
        food='spam', adjective='absolutely horrible'))

    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
          'Dcab: {0[Dcab]:d}'.format(table))

    # passing the table dictionary as keyword arguments with the ** notation.
    able = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
