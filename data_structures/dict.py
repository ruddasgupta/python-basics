def dict_func():
    dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    del dict1['Name'];  # remove entry with key 'Name'
    dict1.clear();  # remove all entries in dict
    del dict1;  # delete entire dictionary

    print("dict['Age']: ", dict['Age'])
    print("dict['School']: ", dict['School'])


if __name__ == '__main__':
    dict_func()
