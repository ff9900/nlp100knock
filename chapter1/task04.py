#coding: utf-8


def task04(string): return {no:word[0] if no in [1, 5, 6, 7, 8, 9, 15, 16, 19] else word[:2] for no, word in enumerate(string[:-1].strip(",.").split(" "), 1)}

if __name__ == "__main__":
    in_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    output = task04(in_string)
    print(output)
