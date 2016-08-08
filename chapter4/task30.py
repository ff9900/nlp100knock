#coding: utf-8


def readlinesFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines


def getSentenseMorphMapList(filename, get_morph_keys):
    import re

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
                # print morph_map_list
                sentense_morph_map_list.append(morph_map_list)
            morph_map_list = list()
        else:
            morph_values = re.split("\t|,", line)
            # infovalues = ["吾輩","名詞","代名詞","一般","*","*","*","吾輩","ワガハイ","ワガハイ""]

            morph_map = dict(zip(morph_keys, morph_values))
            get_morph_map = dict((k, v) for k, v in morph_map.items() if k in get_morph_keys)
            morph_map_list.append(get_morph_map)

    return sentense_morph_map_list

if __name__ == "__main__":
    filename = "neko.txt.mecab"
    get_morph_keys = [
        "surface",
        "pos",
        "pos1",
        "base"
        ]

    sentense_morph_map_list = getSentenseMorphMapList(filename, get_morph_keys)

    print sentense_morph_map_list
