def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e


def example2():
    try:
        int('N/A')
    except ValueError as e:
        print("Couldn't parse:", e)


def example3():
    try:
        int('N / A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None


if __name__ == '__main__':
    try:
        example3()
    except RuntimeError as e:
        print("It didn't work:", e)
        if e.__cause__:
            print('Cause:', e.__cause__)
