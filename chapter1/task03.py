#coding: utf-8


def task03(string):
    words = string[:-1].replace(",", "").replace(".", "").lower().split(" ")
    result = [len(word) for word in words]
    return result

if __name__ == "__main__":
    in_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    output = task03(in_string)
    print(output)
