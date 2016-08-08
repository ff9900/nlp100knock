#coding: utf-8

import re


def readlinesFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines


def getSentenseMorphMapList(filename, get_morph_keys):
    lines = readlinesFile(filename)

    sentense_morph_map_list = list()
    morph_map_list = list()
    morph_keys = [
        "surface",
        "pos",
        "pos1",
        "pos2",
        "pos3",
        "ctype",
        "cform",
        "base",
        "kana",
        "yomi"
        ]

    for line in lines:
        line = line.strip("\n")

        if line == "EOS":
            if morph_map_list != []:
                sentense_morph_map_list.append(morph_map_list)
            morph_map_list = list()
        else:
            morph_values = re.split("\t|,", line)
            morph_map = dict(zip(morph_keys, morph_values))
            get_morph_map = dict((k, v) for k, v in morph_map.items() if k in get_morph_keys)
            morph_map_list.append(get_morph_map)

    return sentense_morph_map_list

if __name__ == "__main__":
    filename = "neko.txt.mecab"
    get_morph_keys = [
        "base",
        "pos",
        ]

    sentense_morph_map_list = getSentenseMorphMapList(filename, get_morph_keys)

    noun_junction_list = list()
    for morph_map_list in sentense_morph_map_list:
        noun_junction = list()
        for morph_map in morph_map_list:
            if morph_map["pos"] == "名詞" and morph_map["base"] != "*":
                noun_junction.append(morph_map["base"])
            else:
                if len(noun_junction) > 1:
                    noun_junction_list.append("".join(noun_junction))
                noun_junction = list()

    for noun_junction in noun_junction_list:
        print noun_junction
