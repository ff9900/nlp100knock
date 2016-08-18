# -*- coding: utf-8 -*-


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def task40():
    morphs_list = list()
    morphs = list()

    for line in open('neko.txt.cabocha', 'r'):
        # * 0 6D 0/1 0.000000
        # 太郎    名詞,固有名詞,人名,名,*,*,太郎,タロウ,タロー B-PERSON
        # は      助詞,係助詞,*,*,*,*,は,ハ,ワ O
        # * 1 2D 0/0 1.468291
        # この    連体詞,*,*,*,*,*,この,コノ,コノ O
        # * 2 4D 0/1 0.742535
        # 本      名詞,一般,*,*,*,*,本,ホン,ホン O
        # を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ O
        # ...
        # EOS
        # ...
        if "\t" in line:
            surface, feature = line.split("\t")
            features = feature.split(",")
            morph = Morph(surface, features[6], features[0], features[1])
            morphs.append(morph)
        elif "EOS" in line:
            if len(morphs) > 1:
                morphs_list.append(morphs)
            morphs = list()

    return morphs_list

if __name__ == '__main__':

    morphs_list = task40()

    for morph in morphs_list[2]:
        print morph.surface,
