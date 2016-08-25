# -*- coding: utf-8 -*-


from ntask41 import ntask41


if __name__ == '__main__':

    lines = open('neko.txt.cabocha', 'r')
    document = ntask41(lines)

    for sentence in document:
        for chunk in sentence:
            if chunk.dst == -1: continue
            print("%s\t%s" % (chunk.get_text(), sentence[chunk.dst].get_text()))
