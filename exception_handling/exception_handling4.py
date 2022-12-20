import sys

print(sys.argv)
for arg in sys.argv[1:]:
    try:
        print(arg)
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
