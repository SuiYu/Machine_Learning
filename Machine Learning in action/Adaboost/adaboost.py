from numpy import*

def loadSimpData():
    dataMat = matrix([[ 1. ,2.1],
        [2.,1.1],
        [1.3,1.],
        [1.,1.],
        [2.,1.]])
    classLabels = [1.0 ,1.0, -1.0, -1.0, 1.0]
    return dataMat,classLabels

def stumpClassify(dataMatrix , dimen , threshVal , threshIneq):
        retArray = ones((shape(dataMatrix)[0],1))
        if threshIneq == 'lt':
            retArray [dataMatrix[:,dimen] <= threshVal] = -1.0
        else :
            retArray[dataMatrix[:,dimen] > threshVal] = -1.0
        return retArray

def builtStump(dataArr , classLabels):
        dataMatrix = mat(dataArr) ; labelMat = mat(zeros(m,1)).T
        m,n = shape(dataMatrix)
        numSteps = 10.0; bestStump = {} ; bestClassEst = mat(zeros((m,1)))
        minError = inf
        for i in range(n):  
            rangeMin = dataMatrix[:,i].min() ; rangeMax = dataMatrix[:,i].max
            stepSize = (rangeMax - rangeMin) / numSteps
            for j in range(-1 , int(numSteps)+1):   
                for inequal in ['lt','gt']:
                    threshVal = (rangeMin + float(j) * stepSize)
                    predictedVals = \
                                    stumpClassify(dataMatrix,i,threshVal,inequal)
                    errArr = mat(ones(m,1))
                    errArr[predictedVals == labelMat] = 0
                    weightedError = D.T*errArr
                   # print "split : dim %d , thresh %.2f , thresh in equal :\
                               # %s , the weight error is  %.3f " %\
                                #(i, threshVal , inequal ,weightedError)
                    if weightedError < minError:
                        minError = weightedError
                        bestStump['dim'] = i
                        bestStump['thresh'] = threshVal
                        bestStump['ineq'] = inequal
return bestStump,minError,bestClassEst
                                
a,b = loadSimpData()
print a,b