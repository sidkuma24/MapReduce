import sys
from sys import argv
import csv
import os
import random
import linecache as lc

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


def main():
    myArgs = getopts(argv);
    nLines = 1000;
    nFeatures = nLines;
    outFile = '';

    if '-i' in myArgs:
            inputFile = myArgs['-i'];
            fileExtn = inputFile.split('.')[1];
            if fileExtn != 'csv' :
                    print '\nError: Incorrect input file, csv file required.\n';
                    return;
            outFile = inputFile.split('.')[0] + '_sample' + '.csv';

    print 'Input data file : ' + inputFile;

    if '-l' in myArgs:
        nLines = int(myArgs['-l']);
        print 'Number of lines in sample file = ' + str(nLines);

    # inF = open(inputFile,'rb');
    outF = open(outFile, 'wb');

    cols = 'feature_1';
    for i in range (2,nFeatures+1):
            colName = 'feature_' + str(i);
            cols = cols + ',' + colName;

        # print cols;
    cols = cols + ',class' + '\n' ;
    outF.writelines(cols);
    
    for line in range(0,nLines):
        lineNo = random.randrange(0,100000);

        row = lc.getline(inputFile,lineNo);
        outF.writelines(row);

    print 'Sample Data File : ' + outFile;


if __name__ == "__main__" : 
    main()
