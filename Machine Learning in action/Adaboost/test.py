from numpy import *

def loadSimpData():
    dataMat = matrix([[ 1. ,2.1],
        [2.,1.1],
        [1.3,1.],
        [1.,1.],
        [2.,1.]])
    classLabels = [1.0 ,1.0, -1.0, -1.0, 1.0]
    return dataMat,classLabels

a,b = loadSimpData()
x =mat(b)
c = mat(a).T
d = x.copy()
print a,c,d