# -*- coding: utf-8 -*-
import re


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs


def task41():
    chunks_list = list()
    chunks = list()
    srcs = dict()

    for line in open('neko.txt.cabocha', 'r'):
        # * 0 3D 0/1 0.000000
        # 太郎    名詞,固有名詞,人名,名,*,*,太郎,タロウ,タロー B-PERSON
        # は      助詞,係助詞,*,*,*,*,は,ハ,ワ O
        # * 1 2D 0/0 1.468291
        # この    連体詞,*,*,*,*,*,この,コノ,コノ O
        # * 2 3D 0/1 0.742535
        # 本      名詞,一般,*,*,*,*,本,ホン,ホン O
        # を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ O
        # * 3 -1D
        # 買っ
        # た
        # EOS
        # ...
        if re.search(r"^\*", line):
            elements = line.split(" ")
            chunk_no = int(elements[1])
            dst = elements[2][:-1]
            chunks.append(Chunk([], dst, srcs))

            if dst != '-1':
                try:
                    srcs[dst].append(chunk_no)
                except:
                    srcs[dst] = list()
                    srcs[dst].append(chunk_no)

        elif "\t" in line:
            surface, feature = line.split("\t")
            features = feature.split(",")
            morph = Morph(surface, features[6], features[0], features[1])
            chunks[chunk_no].morphs.append(morph)

        elif "EOS" in line:
            if len(chunks) == 0: continue
            chunks_list.append(chunks)
            chunks = []
            srcs = {}

    return chunks_list


if __name__ == '__main__':
    chunks_list = task41()
    for chunk, index in zip(chunks_list[2], map(str, range(len(chunks_list[2])))):
        print "index: %s" % index
        print "dst: %s" % chunk.dst
        print "srcs: %s" % (chunk.srcs[index] if index in chunk.srcs else [])
        for morph in chunk.morphs:
            print morph.surface,
        print
        print