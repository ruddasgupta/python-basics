def my_decorator(fn):
    def inner_function():
        fn()
        print('How are you?')

    return inner_function


@my_decorator
def greet():
    print('Hello! ', end='')


if __name__ == '__main__':
    greet()
