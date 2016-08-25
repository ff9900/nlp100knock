# -*- coding: utf-8 -*-

from ClassSet import Morph


def ntask40(lines):
    document = list()
    morphs_list = list()

    for line in lines:
        line = line.strip()
        if "\t" in line:
            surface, feature = line.split("\t")
            features = feature.split(",")
            morph = Morph(surface, features[6], features[0], features[1])
            morphs_list.append(morph)
        elif "EOS" in line:
            if morphs_list == []: continue
            document.append(morphs_list)
            morphs_list = list()
            
    return document


if __name__ == '__main__':

    lines = open('neko.txt.cabocha', 'r')

    document = ntask40(lines)

    sentence_no = 2
    print "/".join(morph.surface for morph in document[sentence_no])
