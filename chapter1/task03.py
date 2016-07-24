#coding: utf-8


def task03(string): return [len(word) for word in string[:-1].strip(",.").split(" ")]

if __name__ == "__main__":
    in_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    output = task03(in_string)
    print(output)
