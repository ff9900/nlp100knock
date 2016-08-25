# -*- coding: utf-8 -*-

from task41 import task41

'''
 digraph graphname {
    a -> b -> c;
    b -> d;
}
'''


def task44(chunks):
    result = list()
    for chunk in chunks:
        chunk_list = list()
        while 1:
            chunk_list.append(''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']))
            if chunk.dst == '-1':
                if len(chunk_list) > 1:
                    if not any([' -> '.join(chunk_list) in r for r in [' -> '.join(rslt) for rslt in result]]):
                        result.append(chunk_list)
                break
            chunk = chunks[int(chunk.dst)]
    return result


if __name__ == '__main__':
    chunks_list = task41()
    chunks = chunks_list[2]
    print "digraph dependency{"
    for phrase in task44(chunks):
        print "    "+" -> ".join(phrase)
    print "}"
