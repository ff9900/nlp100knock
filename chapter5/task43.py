# -*- coding: utf-8 -*-

from task41 import task41


chunks_list = task41()


for chunks in chunks_list:
    for chunk in chunks:
        if chunk.dst != '-1':
            pre = '名詞' in [morph.pos for morph in chunk.morphs]
            suf = '動詞' in [morph.pos for morph in chunks[int(chunk.dst)].morphs]
            if pre and suf:
                phrase = ''
                phrase += ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
                phrase += '\t'
                phrase += ''.join([morph.surface for morph in chunks[int(chunk.dst)].morphs if morph.pos != '記号'])
                print phrase
