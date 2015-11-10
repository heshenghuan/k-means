#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 17:40:32 2015-11-06

@author: heshenghuan (heshenghuan@sina.com)
http://github.com/heshenghuan
"""

from kmeans import KMeans as km

if __name__ == "__main__":
    case = km(1024,10)
    case.read_samples(r"trainDigits.data")
    case.printInfo()
    case.clustering(delta_thrld=0.5)

    case.saveModel()
    case.loadModel()