def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)


if __name__ == '__main__':
    try:
        f()
    except Exception as e:
        print(f'caught {type(e)}: e')
