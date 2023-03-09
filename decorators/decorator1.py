def my_decorator(fn):
    def inner_function():
        fn()
        print('How are you?')

    return inner_function


@my_decorator
def greet():
    print('Hello! ', end='')


# @my_decorator
# def greet_fullname(fn, ln):
#     print(fn + " " + ln + " ", end='')


if __name__ == '__main__':
    # greetings = my_decorator(greet)
    # greetings()
    greet()
    # greet_fullname("Bob", "Dylan")
