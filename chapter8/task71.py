# -*- coding: utf-8 -*-

import re
from nltk.corpus import stopwords


def task71(sentence):
    words = [word.lower() for word in re.sub("[\.\,\!\?;\:\(\)\[\]\'\"]$", '', sentence.rstrip()).split()]
    result = [word for word in words if word in stopwords.words('english')]
    return True if len(result) != 0 else False


if __name__ == '__main__':
    print task71("I am a pen.")
