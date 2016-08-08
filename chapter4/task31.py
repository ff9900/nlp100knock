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
        "surface",
        "pos",
        ]

    sentense_morph_map_list = getSentenseMorphMapList(filename, get_morph_keys)

    flatten_morph_map = [flatten for inner in sentense_morph_map_list for flatten in inner]
    verb_surface_list = [m["surface"] for m in flatten_morph_map if m["pos"] == "動詞"]

    for verb in verb_surface_list:
        print verb
