#coding: utf-8


def task08(string): return "".join(chr(219-ord(c)) if "a"<=c<="z" else c for c in string)

if __name__ == "__main__":
    in_string = "I am an NLPer"
    output = task08(in_string)
    print(output)
    output = task08(output)
    print(output)
