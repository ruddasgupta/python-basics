if __name__ == '__main__':

    # write
    file = open('file.txt', 'w')
    file.write("This is the write command\n")
    file.write("It allows us to write in a particular file")

    # read
    file = open("file.txt", "r")
    print(file.read())

    file.close()
