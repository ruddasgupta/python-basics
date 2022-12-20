if __name__ == '__main__':
    while True:
        try:
            x = int(input("Please enter a number: "))
            print(x)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")