#coding: utf-8


def task07(x, y, z): return u"{}時の{}は{}".format(x, y, z)

if __name__ == "__main__":
    x, y, z = 12, u"気温", 22.4
    output = task07(x, y, z)
    print(output)
