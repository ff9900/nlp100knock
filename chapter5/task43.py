# -*- coding: utf-8 -*-

from task41 import task41


chunks_list = task41()


for chunks in chunks_list:
    for index in range(len(chunks)):
        try:
            pre = '名詞' in [morph.pos for morph in chunks[index].morphs]
            suf = '動詞' in [morph.pos for morph in chunks[index+1].morphs]
            if pre and suf:
                phrase = ''
                phrase += ''.join([morph.surface for morph in chunks[index].morphs if morph.pos != '記号'])
                phrase += '\t'
                phrase += ''.join([morph.surface for morph in chunks[index+1].morphs if morph.pos != '記号'])
                print phrase
        except:
            continue
