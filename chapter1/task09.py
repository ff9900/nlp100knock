#coding: utf-8


def task09(string): return " ".join(word[0]+"".join(__import__("random").sample(list(word[1:-1]), len(list(word[1:-1]))))+word[-1] if len(word) > 4 else word for word in string[:-1].split(" "))

if __name__ == "__main__":
    in_string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    output = task09(in_string)
    print(output)
