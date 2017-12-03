import sys
from sys import argv
import csv
import os


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


def getData(F, nFeatures):
    data_vector = []
    line = F.readline();  
    line_split = line.split();
    # print int(line_split[1]);
    instance_id = int(line_split[1]);
    data_line = F.readline();
    data_line_split = data_line.split();
    instance_class = data_line_split[0];
    #print instance_id ;
    feature_list = [];
    i = 1;
    for count in range(1,nFeatures+1):
        if  i < (len(data_line_split)) and count == int(data_line_split[i].split(':')[0]) : 
            feature_list.insert(count, float(data_line_split[i].split(':')[1]));
           # print 'count = ' + data_line_split[i].split(':')[0]
            i = i+1;
           # print i
        else :
            feature_list.insert(count, 0.00);
    
    feature_list.append(instance_class);
      
    return feature_list;

def main():
    myArgs = getopts(argv);
   
    
    if '-i' in myArgs:
        trainFile = myArgs['-i'];
        print "Input File : " + trainFile; 

    if '-o' in myArgs:
        dataFile = myArgs['-o'];
        print "Data File : " + dataFile; 


    F1 = open(trainFile, "rb")
    F = open(trainFile, "rb")
   
    outF = open(dataFile, 'w');    

    nFeatures = 1000;
    count  = 0;
    dataset = [];
    cols = 'feature_1';
    for j in range (2,nFeatures+1):
        colName = 'feature_' + str(j);
        cols = cols + ',' + colName;

    # print cols;
    cols = cols + ',class' + '\n' ;
    outF.writelines(cols);

    for line in F:
        instance = getData(F1, nFeatures);
        dataset.insert(count,instance);
        outline = ', '.join(str(x) for x in dataset[count]);
        count = count+1;
        outF.writelines(outline);
        outF.writelines('\n');


if __name__ == "__main__" : 
    main()
