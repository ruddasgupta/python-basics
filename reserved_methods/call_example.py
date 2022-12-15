class Entity:
    '''Callable to update the entity's position.'''

    def __init__(self, x, y):
        print("__init__")
        self.x, self.y = x, y

    def __call__(self, x, y):
        '''Change the position of the entity.'''
        print("__call__")
        self.x, self.y = x, y


if __name__ == '__main__':
    point = Entity(10, 20)
    print(point.x, point.y)
    point(30, 40)
    print(point.x, point.y)
