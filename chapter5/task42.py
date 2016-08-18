# -*- coding: utf-8 -*-

from task41 import task41


def task42(chunks):
    result = []
    for chunk in chunks:
        if chunk.dst != '-1':
            phrase = ''
            phrase += ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
            phrase += '\t'
            phrase += ''.join([morph.surface for morph in chunks[int(chunk.dst)].morphs if morph.pos != '記号'])
            result.append(phrase)
    return result


if __name__ == '__main__':

    chunks_list = task41()
    for chunks in chunks_list:
        for phrase in task42(chunks):
            print phrase
        print
