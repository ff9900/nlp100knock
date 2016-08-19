#!/usr/bin/python
# coding: UTF-8


def readlinesFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return(lines)


def Morphol(filename):
    import re
    lines = readlinesFile(filename)

    result = list()  # 1文づつのリストを格納
    mecabinfos = list()  # 1単語づつの辞書型のリストを格納
    infokeys = ["surface", "pos", "pos1", "pos2", "pos3", "ctype", "cform", "base", "kana", "yomi"]
    for line in lines:
        line = line.strip("\n")

        if line == "EOS":
            if mecabinfos != []:
                result.append(mecabinfos)
                mecabinfos = list()

        else:
            infovalues = re.split("\t|,", line)
            infodicts = dict(zip(infokeys, infovalues))  # keyとvaluseを引っ付ける
            # getinfodicts = dict((k, v) for k, v in infodicts.items() if k in getinfos)
            mecabinfos.append(infodicts)

    return result


def n_succession(dists):
    result = list()
    n_succ = list()
    L = 0

    for dist in dists:
        if(dist["pos"] == "名詞" and dist["base"] != "*"):
            n_succ.append(dist["base"])
        else:
            l = len(n_succ)
            if l > L:
                L = l
                wo = "".join(n_succ)
                result = [L, wo]
            n_succ = list()
    return result


if __name__ == "__main__":
    filename = "neko.txt.mecab"  # 読み込むファイル名
    # getinfos = ["surface", "pos", "base"]  # 欲しい辞書のkey
    output = Morphol(filename)  # 1行毎に辞書型になったリストを返す
    # print output[:10]

    for dists in output:
        r = n_succession(dists)  # 名詞の連接（連続して出現する名詞）を最長一致で抽出
        if r != [] and r[0] > 1:
            print r[0], r[1]

