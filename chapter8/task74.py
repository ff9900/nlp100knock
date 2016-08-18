# -*- coding: utf-8 -*-

import numpy
from task72 import task72, stemming
from task73 import task73


if __name__ == '__main__':

    features = task72()
    words, model = task73(features)

    # sentence = "I'm very happy to hear your presentation was a success ."
    sentence = "It is sad that so few people give money to help the hunger ."
    input_vec = numpy.zeros(len(words))

    for word in stemming(sentence):
        try:
            index = words.index(word)
            input_vec[index] += 1
        except:
            continue

    print model.predict(input_vec)
    print model.predict_proba(input_vec)
