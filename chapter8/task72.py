# -*- coding: utf-8 -*-

import re
from nltk.corpus import stopwords
import nltk


def stemming(sentence):
    st = nltk.PorterStemmer()
    words = [st.stem(word.lower()) for word in re.sub("[\.\,\!\?;\:\(\)\[\]\'\"]$", '', sentence.rstrip()).split()]
    words = [word for word in words if word not in stopwords.words('english')]
    return words


def task72():

    features = []

    for line in open('sentiment.txt', 'r'):
        label = line[:2]
        for word in stemming(line[3:]):
            features.append([label, word])

    return features


if __name__ == '__main__':

    features = task72()

    print len([feature for feature in features if feature[0] == '-1'])
    print len([feature for feature in features if feature[0] == '+1'])
