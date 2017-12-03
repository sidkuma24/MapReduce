## Using these Scripts:

#### Download the youtube video dataset
```
mkdir dataset

curl http://archive.ics.uci.edu/ml/machine-learning-databases/00269/dir_data.tar -o ./dataset/dir_data.tar 

tar -xvf ./datasest/dir_data.tar

cd ./dataset/dir_data/

gunzip ./test/*
gunzip  ./train/*
gunzip  ./validation/*

```

#### Process Data to get CSV for WEKA


```
python preProcess.py -i [input data file] -o [output file name]

```
* input data file - input txt file from the dataset
* output file name - name of the output csv file that is created. example - sample.csv


##### Get random samples from the CSV file

```
python getSampleData.py -i [input data file] -l [no of lines]
```

