class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = Distance()
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __str__(self):
        return 'ft:' + str(self.ft) + ' in: ' + str(self.inch)


if __name__ == '__main__':
    d1 = Distance(3, 10)
    d2 = Distance(4, 4)
    print("d1= {} d2={}".format(d1, d2))
    d3 = d1 + d2
    print(d3)
