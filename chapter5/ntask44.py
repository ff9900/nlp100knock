# -*- coding: utf-8 -*-


from ntask41 import ntask41


if __name__ == '__main__':

    lines = open('neko.txt.cabocha', 'r')
    document = ntask41(lines)

    sentence_no = 0
    sentence = document[sentence_no]

    # 一つずつ
    print("digraph graphname {")
    for chunk in sentence:
        if chunk.dst != -1:
            print("  {0} -> {1}" .format(chunk.get_text(), sentence[chunk.dst].get_text()))
    print("}")

    # まとめて
    result = list()
    for chunk in sentence:
        tmp = list()
        while 1:
            tmp.append(chunk.get_text())
            if chunk.dst == -1:
                if len(tmp) > 1:
                    if not any([' -> '.join(tmp) in ' -> '.join(r) for r in result]):
                        result.append(tmp)
                break
            chunk = sentence[chunk.dst]

    print "digraph graphname {"
    for r in result:
        print ' -> '.join(r)
    print "}"
