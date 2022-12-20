if __name__ == '__main__':

    # write
    with open("file2.txt", "w") as f:
        f.write("Hello World!")

    # read
    with open("file2.txt") as file:
        data = file.read()
        print(data)

    file.close()
