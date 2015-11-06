# k-means algorithm

###Introduction
> An python implementation of k-means clustering algorithm.<br>
> Using numpy.array model to represent matrix and vector.<br>

##Data format
The format of training and testing data file must be:<br>

\<label> \<index1>:\<value1> \<index2>:\<value2> . . .<br>
.<br>
.<br>
.<br>

Each line contains an instance and is ended by a '\n' character. \<label> and \<index>:\<value> are sperated by a '\t' character. But \<index>:\<value> and 
\<index>:\<value> are sperated by a ' ' character.<br>

\<label> is an indicator indicating the class id. Usually the indicator is an integer or a character.<br>

- Integer:<br>The range of class id should be from 0 to the size of classes subtracting one. For example, the class id is 0, 1, 2 or 3 for a 4-class classification problem.<br>
- Character:<br>
The class id should be a single character. For example, the class id can be 'B',
'M', 'E', 'S' in character-based Chinese Word Segmentation.

**The \<label> indicator is useless in clustering algorithm, so you can just ignore this label. You can put any character in here, and the program will just ignoring it.**
 
\<index> is a postive integer denoting the feature id. The range of feature id should be from 1 to the size of feature set.

- For example, the feature id is 1, 2, ... 9 or 10 if the dimension of feature set is 10. 

\<value> is a float denoting the value of feature.


If the feature value equals 0, the <index>:<value> is encourged to be neglected
for the consideration of storage space and computational speed.

Labels in the testing file are only used to calculate accuracy or errors. 
If they are unknown, just fill the first column with any class labels.

##Usage

> You can see all the cases in test.py

#### Create an instance
		# create an instance of softmaxreg
		>>> from kmeans import KMeans as km
		>>> case = km(1024,10)
		
		
#### Read training file		
		# read training file
		>>> case.read_samples(r"train.data")
		Loading samples...
		100 ... 200 ... 300 ... 400 ... 500 ... 600 ... 700 ... 800 ... 900 ... 
		1000 ... 1100 ... 1200 ... 1300 ... 1400 ... 1500 ... 1600 ... 1700 ... 
		1800 ... 1900 ...
		Loaded 1934 samples!

#### Print information
		# print information of this model
		>>> case.printinfo()
		sample size:       1934
		clusters size:     10
		feature dimension: 1024

#### Clustering
		
		#### Clustering
		>>> case.clustering(delta_thrld=0.5)
		Running clustering algorithm...
		Iter    1
		The difference bwteen new centers and old centers:
		clus  1: 9.2919
		clus  2: 8.5926
		clus  3: 8.0302
		clus  4: 8.3112
		clus  5: 7.9715
		clus  6: 8.7807
		clus  7: 9.1319
		clus  8: 8.0467
		clus  9: 9.1051
		clus 10: 7.8327
		.
		.
		.
		Iter    9
		The difference bwteen new centers and old centers:
		clus  1: 0.1752
		clus  2: 0.1795
		clus  3: 0.1418
		clus  4: 0.1053
		clus  5: 0.1367
		clus  6: 0.4836
		clus  7: 0.0000
		clus  8: 0.0751
		clus  9: 0.0634
		clus 10: 0.0000
		Reach the minimal change value threshold!
		
		The center of each cluster is:
		
		clus  1: [[ 0.  0.  0. ...,  0.  0.  0.]]
		clus  2: [[ 0.  0.  0. ...,  0.  0.  0.]]
		clus  3: [[ 0.  0.  0. ...,  0.  0.  0.]]
		clus  4: [[ 0.  0.  0. ...,  0.  0.  0.]]
		clus  5: [[ 0.  0.  0. ...,  0.  0.  0.]]
		clus  6: [[ 0.  0.  0. ...,  0.  0.  0.]]
		clus  7: [[ 0.  0.  0. ...,  0.  0.  0.]]
		clus  8: [[ 0.          0.          0.         ...,  0.00719424  0.00239808  0.00239808]]
		clus  9: [[ 0.          0.          0.         ...,  0.07179487  0.02564103  0.01538462]]
		clus 10: [[ 0.  0.  0. ...,  0.  0.  0.]]
		
		Totally used 9 round to finished clustering process.
