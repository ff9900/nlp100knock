# -*- coding: utf-8 -*-

from ClassSet import Chunk, Morph
from collections import defaultdict


def ntask41(lines):
    documents = list()
    chunk_list = list()
    srcs = defaultdict(list)

    for line in lines:
        line = line.strip()
        if line.startswith('* '):
            elements = line.split(" ")
            chunk_id = int(elements[1])
            dst = int(elements[2].replace('D', ''))
            chunk_list.append(Chunk(id=chunk_id, morphs=[], dst=dst, srcs=[]))
            srcs[dst].append(chunk_id)
        elif "\t" in line:
            surface, feature = line.split("\t")
            features = feature.split(",")
            morph = Morph(surface, features[6], features[0], features[1])
            chunk_list[-1].morphs.append(morph)
        elif line == 'EOS':
            for chunk_id, src in srcs.items():
                if chunk_id == -1: continue
                chunk_list[chunk_id].srcs = src
            documents.append(chunk_list)
            chunk_list = []
            srcs = defaultdict(list)

    return documents


if __name__ == '__main__':

    lines = open('neko.txt.cabocha', 'r')

    documents = ntask41(lines)

    sentence_no = 2
    for chunk in documents[sentence_no]:
        print(chunk.__str__())
