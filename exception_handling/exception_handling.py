class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


if __name__ == '__main__':
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")
