#coding: utf-8


def str_ngram(string, n): return [string[i:i+n] for i in xrange(len(string)-n+1)]


def word_ngram(string, n): return [" ".join(string.split(" ")[i:i+n]) for i in xrange(len(string.split(" "))-n+1)]

if __name__ == "__main__":
    in_string = "I am an NLPer"
    n = 2
    output = str_ngram(in_string, n)
    print(output)
    output = word_ngram(in_string, n)
    print(output)
