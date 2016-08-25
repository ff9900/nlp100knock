# -*- coding: utf-8 -*-

from task41 import task41


def task45(sentence):
    result = list()
    for chunk in sentence:
        chunk_list = list()
        while 1:
            chunk_list.extend([morph.surface for morph in chunk.morphs if morph.pos == '動詞'])
            if chunk.dst == '-1':
                print chunk_list
                if len(chunk_list) > 1:
                    if not any([' -> '.join(chunk_list) in r for r in [' -> '.join(rslt) for rslt in result]]):
                        result.append(chunk_list)
                break
            chunk = sentence[int(chunk.dst)]
    return result


if __name__ == '__main__':
    document = task41()
    sentence = document[0]
    print "digraph dependency{"
    for phrase in task45(sentence):
        print "    "+" -> ".join(phrase)
    print "}"
