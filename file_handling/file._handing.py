if __name__ == '__main__':
    f = open('workfile', 'rb+')
    print(f.write(b'0123456789abcdef'))
    print(f.seek(5))  # Go to the 6th byte in the file
    print(f.read(1))
    print(f.seek(-3,2))  # Go to the 3rd byte before the end
    print(f.read(1))
