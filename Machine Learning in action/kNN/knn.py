from numpy import *
from os import listdir
import operator

def CreatDataSet() :
	group = array([[1.0,1.1],[1,1],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def  classify(inX,dataSet,labels,k):
	Size = dataSet.shape[0]
	diffmat = tile(inX, (Size,1)) - dataSet
	sqdiffmat = diffmat**2
	sqdistace = sqdiffmat.sum(axis = 1)
	distance = sqdistace**0.5
	sortedDistanceIndicies = distance.argsort()
	classCount = {}
	for i in range(k) :
		voteIlabel = labels [sortedDistanceIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
	sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]
	
def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayOLines :
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append( int(listFromLine[-1] ))
		index += 1
	return returnMat,classLabelVector

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet / tile (ranges,(m,1))
	return normDataSet , ranges , minVals

def datingClassTest():
	hoRatio = 0.10
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int (m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs) :
		classifierResult = classify(normMat[i,:] , normMat[numTestVecs:m,:],\
			datingLabels[numTestVecs:m],3)
		print "The classifier came back wiith : %d the real answer is : %d " \
		% (classifierResult, datingLabels[i])
		if  (classifierResult != datingLabels[i]) :
			errorCount += 1
	print "the total error rate is : %f" % (errorCount / float(numTestVecs))

def img2vector(filename):
	returnVect = zeros ((1,1024))
	fr = open(filename)
	for i in range(32) :
		lineStr = fr.readline()
		for j in range (32) :
			returnVect[0,32*i+j] = int (lineStr[j])
	return returnVect

def HandWritingClassTest():
	hwLabels = []
	trainingFileList = listdir('trainingDigits')
	m =len(trainingFileList)
	trainingMat = zeros ((m,1024))
	for i in range(m) :
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int (fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector('trainingDigits/%s' %fileNameStr)
	testFileList = listdir('testDigits')
	errorCount=0.0
	mTest = len(testFileList)
	for i in range(mTest) :
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
		classifierResult = classify(vectorUnderTest, \
			trainingMat,hwLabels,3)
		print "the classifier come back with : %d,and the real answer is : %d" % (classifierResult,classNumStr)

		if (classifierResult != classNumStr) :
			errorCount += 1.0
	print "\nThe total number of error is %d" % errorCount
	print "\n The error rate is %f" % (errorCount/float(mTest))