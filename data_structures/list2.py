if __name__ == '__main__':
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print('Count Apple ', fruits.count('apple'))
    print('Count tangerine ', fruits.count('tangerine'))
    print('Index Banana ', fruits.index('banana'))
    print('Index Banana After Index 4 ', fruits.index('banana', 4))  # Find next banana starting at position 4
    fruits.reverse()
    print('Reversed -> ',fruits)
    fruits.append('grape')
    print('Append grape -> ', fruits)
    fruits.sort()
    print('Sorted -> ', fruits)
    print('Pop -> ', fruits.pop())
