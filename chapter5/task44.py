# -*- coding: utf-8 -*-

import task41
import task42
import re


chunks_list = task41.task41()
chunks = chunks_list[2]

'''
 digraph graphname {
    a -> b -> c;
    b -> d;
}
'''

print "digraph dependency{"
for phrase in task42.task42(chunks):
    print "    %s;" % re.sub('\t', ' -> ', phrase)
print "}"
