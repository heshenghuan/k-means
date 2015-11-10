#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 14:52:39 2015-11-03

@author: heshenghuan (heshenghuan@sina.com)
http://github.com/heshenghuan
"""

import codecs
import math
import random
import numpy as np

class KMeans:
    def __init__(self, dimension=0, k_val=2):
        self.K = k_val # the k value of clusters num
        self.feat_dimension = dimension # the degree of features
        self.samples = None
        self.clusters = None # the k clusters of samples
        self.centers = None # the mean value of each cluster i.e. the center of cluster
        
    def printInfo(self):
        print "sample size:      ", len(self.samples)
        print "clusters size:    ", self.K
        print "feature dimension:", self.feat_dimension

    def read_samples(self, datafile=None):
        if not datafile:
            print "Not given any file path to load samples."
            return False
        
        try:
            data = codecs.open(datafile, 'r')
            num = 0
            self.samples = []
            print "Loading samples..."
            for line in data.readlines():
                val = line.strip().split('\t')
                # max_index = 0
                val = val[-1].split(" ")
                sample_vec = {}
                for i in range(len(val)):
                    [index, value] = val[i].split(':')
                    sample_vec[int(index)] = float(value)
                self.samples.append(sample_vec)
                num += 1
                if num%100==0 and num != 0:
                    print num,"...",
            print
            print "Loaded %d samples!"%num
            # self.label_set = list(set(self.label_list))
            return True
        except IOError:
            print "Error:File does"
            print "Training data file \"",filepath,"\" doesn\'t exist!"
            return False

    def __getSampleVec(self, sample):
        """
        Returns a row vector by 1*(n+1).
        """
        sample_vec = np.zeros((1,self.feat_dimension+1))
        for i in sample.keys():
            sample_vec[0][i] = sample[i]

        return sample_vec

    def __getDistance(self, sample):
        """
        Returns a list of distance between sample and each center.
        """
        distance = []
        samp = self.__getSampleVec(sample)
        for i in xrange(self.K):
            center = self.centers[i]
            dist = math.sqrt(sum(sum((samp - center)*(samp - center))))
            distance.append(dist)

        return distance

    def randomInit(self):
        """
        Random initialization function. Random choose k samples as centers.
        """
        self.centers = []
        m = len(self.samples)
        id_list = []
        while len(id_list)<=self.K:
            index = random.randint(0,m-1)
            if not index in id_list:
                id_list.append(index)
        for i in id_list:
            self.centers.append(self.__getSampleVec(self.samples[i]))

    def assignPoints(self):
        """
        Assigns a cluster to each sample and records the index of each cluster.
        """
        m = len(self.samples)
        self.clusters = []
        for j in xrange(self.K):
            self.clusters.append([])

        for i in xrange(m):
            distance = self.__getDistance(self.samples[i])
            c = distance.index(min(distance))
            self.clusters[c].append(i)

    def updateCenter(self):
        """
        Updates the centers value of each cluster.
        """
        self.centers = []
        for i in xrange(self.K):
            point_sum = np.zeros((1,self.feat_dimension+1))
            for j in self.clusters[i]:
                vec = self.__getSampleVec(self.samples[j])
                point_sum += vec
            point_sum /= len(self.clusters[i])
            self.centers.append(point_sum)

    def printCenter(self):
        for i in xrange(self.K):
            print "clus %2d:"%(i+1), self.centers[i]

    def clustering(self, max_iter=100, delta_thrld=0.1):
        """
        The clustering algorithm.

        max_iter: the maximum number of iteration(default 100).
        delta_thrld: the threshold of centers value(default 0.01) change, and the 
        signal of training finished.
        """
        print "\nRunning clustering algorithm..."
        self.randomInit()
        rd = 1
        while rd <= max_iter:
            self.assignPoints()
            oldCenters = self.centers
            self.updateCenter()
            
            print "Iter %4d   "%rd
            print "The difference bwteen new centers and old centers:"
            delta = []
            for i in xrange(self.K):
                delta.append(math.sqrt(sum(sum((self.centers[i] - oldCenters[i])*(self.centers[i] - oldCenters[i])))))
                print "clus %2d:"%(i+1), "%.4f"%delta[i]
            
            rd += 1
            if sum(delta)/len(delta) < delta_thrld:
                print "Reach the minimal change value threshold!"
                print "\nThe center of each cluster is:\n"
                self.printCenter()
                break

        print "\nTotally used %d round to finished clustering process."%(rd-1)

    def saveModel(self, path=None):
        """
        Saves the model as a text file by following format:

        K=<value> D=<value>
        <center> <index1>:<value1> <index2>:<value2> ...
        .
        .
        .
        In the first line, the K and D mean the k value and feature dimension,
        respectively.
        Each line contains an instance and is ended by a '\\n' character. 
        <center> and <index>:<value> are sperated by a '\\t' character. 
        But <index>:<value> and <index>:<value> are sperated by a \' \' character.

        Parameter path is the directory path where you want to save the model.
        """
        if not path:
            path = r'./'
        output = open(path+r"centers.utf8",'w')
        output.write("K=%d Dimension=%d\n"%(self.K,self.feat_dimension))
        for i in xrange(self.K):
            index = "%d"%(i+1)
            output.write(index+"\t")
            center = self.centers[i]
            for j in xrange(1,self.feat_dimension+1):
                if center[0,j] != 0.:
                    output.write("%d:%f "%(j,center[0,j]))
            output.write('\n')

    def loadModel(self, path=None):
        """
        Load model from file. The file shoud comply with the following format.

        K=<value> D=<value>
        <center> <index1>:<value1> <index2>:<value2> ...
        .
        .
        .
        In the first line, the K and D mean the k value and feature dimension,
        respectively.
        Each line contains an instance and is ended by a '\\n' character. 
        <center> and <index>:<value> are sperated by a '\\t' character. 
        But <index>:<value> and <index>:<value> are sperated by a \' \' character.

        Parameter path is the directory path where you want to save the model.
        """
        if not path:
            path = r'./'
        input_data = codecs.open(path+r"centers.utf8",'r','utf-8')
        first = True
        self.centers = []
        self.K = 0
        self.feat_dimension = 0
        print "Loading centers data from file",
        for line in input_data.readlines():
            rawText = line.strip()
            if first:
                tmp = rawText.split()
                self.K = int(tmp[0].split('=')[1])
                self.feat_dimension = int(tmp[1].split('=')[1])
                first = False
                continue
            tmp = rawText.split('\t')
            tmp = tmp[-1].split(' ')
            vec = np.zeros((1,self.feat_dimension+1))
            for i in xrange(len(tmp)):
                [index, value] = tmp[i].split(':')
                vec[0,int(index)] = float(value)
            self.centers.append(vec)
            print '.',
        print
        print "Loading done."
        self.printCenter()

