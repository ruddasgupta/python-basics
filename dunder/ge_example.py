class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __ge__(self, x):
        val1 = self.ft * 12 + self.inch
        val2 = x.ft * 12 + x.inch
        if val1 >= val2:
            return True
        else:
            return False


if __name__ == '__main__':
    d1 = Distance(2, 1)
    d2 = Distance(4, 10)
    print(d1 >= d2)
    print(d2 >= d1)
