def greet(**person):
    print('Hello ', person['firstname'], person['lastname'])


if __name__ == '__main__':
    greet(firstname='Steve', lastname='Jobs')
    greet(lastname='Jobs', firstname='Steve')
    greet(firstname='Bill', lastname='Gates', age=55, salaey=9000.00)
    # greet(firstname='Bill')  # raises KeyError
