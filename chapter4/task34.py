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
        "base",
        "pos",
        ]

    sentense_morph_map_list = getSentenseMorphMapList(filename, get_morph_keys)

    noun_phrase_list = list()
    for morph_map_list in sentense_morph_map_list:
        for i in xrange(len(morph_map_list)-2):
            m0 = morph_map_list[i]
            m1 = morph_map_list[i+1]
            m2 = morph_map_list[i+2]
            pos_flag = (m0["pos"] == "名詞" and m1["pos"] == "助詞"and m2["pos"] == "名詞")
            word_flag = (m0["base"] != "*" and m1["base"] == "の" and m1["base"] != "*")
            if pos_flag and word_flag:
                noun_phrase_list.append(m0["base"]+m1["base"]+m2["base"])

    for noun_phrase in noun_phrase_list:
        print noun_phrase
