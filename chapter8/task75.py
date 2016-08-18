# -*- coding: utf-8 -*-
# 未完成

from task72 import task72
from task73 import task73


if __name__ == '__main__':

    features = task72()
    words, model = task73(features)

    print model.class_weight
