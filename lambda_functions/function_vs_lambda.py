def cube(y):
    print(f"Finding cube of number:{y}")
    return y ** 3


if __name__ == '__main__':
    lambda_cube = lambda num: num ** 3

    # invoking simple function
    print("invoking function defined with def keyword:")
    print(cube(30))
    # invoking lambda function
    print("invoking lambda function:", lambda_cube(30))
