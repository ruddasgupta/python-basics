if __name__ == '__main__':
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print(tel)
    print(tel['jack'])
    del tel['sape']
    tel['irv'] = 4127
    print(tel)
    print(list(tel))
    print(sorted(tel))
    print('guido' in tel)
    print('jack' not in tel)

    tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(tel2)

    num = {x: x ** 2 for x in (2, 4, 6)}
    print(num)

    tel3 = dict(sape=4139, guido=4127, jack=4098)
    print(tel)
