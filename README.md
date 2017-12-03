# CS267-Project

## Running K-means on Hadoop Cluster


* Make Sure that the Hadoop server is running

#### Preparing Input Directories

```
hadoop fs -mkdir /mahout_data
hadoop fs -mkdir /kmeans_output
hadoop fs -mkdir /mahout_seq
```

* Verify the created directories using:
```
hadoop fs -ls
```


#### Copy the Input file to HDFS
```
hadoop fs -put ./keyVal.txt /mahout_data/
```

* Note: sample.txt file is in hadoop/data/ directory of this repo.

### Converting the txt file to Sequence file
```
mahout seqdirectory \
-i /mahout_data \
-o /mahout_seq \
-ow
                    
```

#### Seq to sparse convertion

```
mahout seq2sparse -i /mahout_seq/ -o /mahout_sparse/ -ow
```


### Perform Canopy Clustering

```
mahout canopy -i /mahout_sparse/tf-vectors -o /canopy_output/ \
-dm org.apache.mahout.common.distance.EuclideanDistanceMeasure -t1 10 -t2 20 -ow

```

### Finally run kmeans using output of Canopy for initial clusters

```
mahout kmeans -i /mahout_sparse/tfidf-vectors \
-c /canopy_output  \
-o /kmeans_output  \
-dm org.apache.mahout.common.distance.EuclideanDistanceMeasure -x 2 -k 30 -ow

```
