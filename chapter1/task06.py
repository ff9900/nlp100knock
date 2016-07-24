#coding: utf-8


def str_ngram(string, n): return [string[i:i+n] for i in xrange(len(string)-n+1)]

if __name__ == "__main__":
    in_string1 = "paraparaparadise"
    in_string2 = "paragraph"
    n = 2
    X = set(str_ngram(in_string1, n))
    Y = set(str_ngram(in_string2, n))
    print(X | Y)
    print(X & Y)
    print(X - Y)
    print(Y - X)
    print("se" in X)
    print("se" in Y)
