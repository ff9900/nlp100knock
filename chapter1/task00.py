#coding: utf-8


def task00(string):
    result = string[-1::-1]
    return result

if __name__ == "__main__":
    in_string = "stressed"
    output = task00(in_string)
    print(output)
