#coding: utf-8


def task01(string):
    result = string[1::2]
    return result

if __name__ == "__main__":
    in_string = u"パタトクカシーー"
    output = task01(in_string)
    print(output)
