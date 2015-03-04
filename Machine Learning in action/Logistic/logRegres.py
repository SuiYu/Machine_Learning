from numpy import*

def loadDataSet():
	dataMat = [ ]; labelMat = [ ];
	fr = open('testSet.txt')
	for line in fr .readlines() :
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat

def sigmoid(inX):
	return 1.0 /(1 + exp(-inX))

def gradAscent(dataMatIn , classLable):
	dataMatrix = mat(dataMatIn)
	labelMat = mat(classLable).transpose()
	m,n = shape(dataMatrix)
	alpha = 0.001
	maxCycles = 500
	weight = ones((n,1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix*weight)
		error = (labelMat -h)
		weight = weight + alpha * dataMatrix.transpose() * error
	return weight

def plotBestFit(wei):
	import matplotlib.pyplot as plt 
	weight = wei
	dataMat,labelMat = loadDataSet()
	dataArr = array(dataMat)
	n = shape(dataArr)[0]
	xcord1 = [ ] ; ycord1 = [ ];
	xcord2 = [ ] ; ycord2 = [ ];
	for i in range(n):
		if int(labelMat[i]) == 1:
			xcord1.append(dataArr[i,1]) ; ycord1.append(dataArr[i,2])
		else :
			xcord2.append(dataArr[i,1]) ; ycord2.append(dataArr[i,2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1 , ycord1 , s=30 , c = 'red' , marker = 's')
	ax.scatter(xcord2 , ycord2 , s=30 , c ='green')
	x = arange (-3.0,3.0,0.1)
	y = (-weight[0]-weight[1]*x) / weight[2]
	ax.plot(x,y)
	plt.xlabel('X1') ; plt.ylabel('X2') ; 
	plt.show()

def stocGradAscent(dataMatrix , classLable):
	m,n = shape(dataMatrix)
	alpha = 0.01
	weight = ones(n)
	for i in range(m):
		h = sigmoid(sum(dataMatrix * weight))
		error = classLable[i] - h
		weight = weight +alpha * error * dataMatrix[i]
	return weight

def  stocGradAscent1(dataMatrix,classLable,numIter = 150):
	m,n = shape(dataMatrix)
	weight = ones(n)
	for j in range(numIter):	
		dataIndex = range(m)
		for i in range(m):
			alpha = 4 /(1.0 + j + i) + 0.01
			randIndex = int(random.uniform(0,len(dataIndex)))
			h =sigmoid(sum(dataMatrix[randIndex]*weight))
			error = classLable[randIndex] - h
			weight = weight +alpha * error * dataMatrix[randIndex]
			del(dataIndex[randIndex])
	return weight


def classifyVector(inX , weight):
	prob = sigmoid(sum(inX*weight))
	if prob > 0.5:
		return 1.0
	else :
		return 0.0

def colicTest():
	frTrain = open('horseColicTraining.txt')
	frTest = open('horseColicTest.txt')
	trainingSet  = [ ] ; trainingLabel = [ ]
	for line in frTrain.readlines():
	 	currLine = line.strip().split('\t')
	 	lineArr = [ ]
	 	for i in range(21):
	 		lineArr.append(float(currLine[i]))
	 	trainingSet.append(lineArr)
	 	trainingLabel.append(float(currLine[21]))
	trainWeights = stocGradAscent1(array(trainingSet),trainingLabel,500)
	errorCount = 0 ; numTestVec = 0.0
	for line in frTest.readlines():
		numTestVec += 1.0
	 	currLine = line.strip().split('\t')
		lineArr = [ ]
		for i in range(21):
			lineArr.append( float(currLine[i]))
		if int(classifyVector(array(lineArr),trainWeights)) != int(currLine[21]):
			errorCount += 1
	errorRate = (float(errorCount)/numTestVec)
	print "The error rate of test is :%f" %errorRate
	return errorRate

def multiTest():
	numTests = 10 ; errorsum = 0.0;
	for k in range (numTests) :
		errorsum += colicTest()
	print "after %d iterationg the average error rate is : %f" %(numTests,errorsum/float(numTests))



























