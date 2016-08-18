# -*- coding: utf-8 -*-

import random


def task70():
    neg = ["-1 %s" % line.rstrip() for line in open('rt-polarity.neg', 'r')]
    pos = ["+1 %s" % line.rstrip() for line in open('rt-polarity.pos', 'r')]
    train = neg + pos
    random.shuffle(train)

    output = open('sentiment.txt', 'w')

    for t in train:
        output.write("%s\n" % t)

    output.close()

    return train

if __name__ == '__main__':

    train = task70()

    print "pos: %s" % len(filter(lambda x: x[:2] == '+1', train))
    print "neg: %s" % len(filter(lambda x: x[:2] == '-1', train))
