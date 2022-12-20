def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


if __name__ == '__main__':
    divide(1, 2)
    divide(1, 0)
    # divide("1", "2")
    divide(1.03, 2.0)