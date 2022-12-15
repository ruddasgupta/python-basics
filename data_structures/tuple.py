def tup_func():
    tup1 = ('physics', 'chemistry', 1997, 2000)
    print(tup1)
    del tup1[2]
    print("After deleting value at index 2 : ")
    print(tup1)


if __name__ == '__main__':
    tup_func()
