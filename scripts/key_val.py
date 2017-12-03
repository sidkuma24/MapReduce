import random

def main():
	n = 10000;
	outFileName = 'keyVal.txt';
	outF = open(outFileName,'wb');

	for i in range(1,n):
		line = str(i) + "," + str(random.randrange(0,100000)) + "\n";
		outF.writelines(line);

	print "File created : keyVal.txt";


if __name__ == "__main__" :
	main()