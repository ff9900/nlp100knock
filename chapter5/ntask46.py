# -*- coding: utf-8 -*-
# みかん

from ntask41 import ntask41

if __name__ == '__main__':
    lines = open('neko.txt.cabocha', 'r')
    document = ntask41(lines)

    sentence_no = 0
    sentence = document[sentence_no]

    for chunk in sentence:
        if '動詞' in [m.pos for m in chunk.morphs]:

            verb = [m.base for m in chunk.morphs if m.pos == '動詞'][0]
            phrases = []

            for src in chunk.srcs:
                if '助詞' in [m.pos for m in sentence[src].morphs]:
                    phrase = sentence[src].get_text()
                    case = [m.base for m in sentence[src].morphs if m.pos == '助詞'][-1]
                    phrases.append((case, phrase))

            if phrases:
                phrases.sort()
                print("%s\t%s\t%s" % (verb, '/'.join([p[0] for p in phrases]), '/'.join([p[1] for p in phrases])))