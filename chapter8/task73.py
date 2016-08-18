# -*- coding: utf-8 -*-

import numpy
from task72 import task72
from sklearn import linear_model


def task73(features):

    features = numpy.array(features)
    words = list(set(features[:, 1]))

    pos_vec = numpy.zeros(len(words))
    neg_vec = numpy.zeros(len(words))

    for feature in features:
        index = words.index(feature[1])
        if feature[0] == '-1':
            pos_vec[index] += 1
        else:
            neg_vec[index] += 1

    model = linear_model.LogisticRegression()
    model.fit([pos_vec, neg_vec], [1, -1])

    return (words, model)


if __name__ == '__main__':

    logit = linear_model.LogisticRegression()
    features = task72()
    words, model = task73(features)
