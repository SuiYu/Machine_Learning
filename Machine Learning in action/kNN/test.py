import knn
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

#datingDataMat,datingLabels= knn.file2matrix('datingTestSet2.txt')

"""
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],
	15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
"""

"""
normMat,ranges,minVals = knn.autoNorm(datingDataMat)
print  normMat
"""
"""
# knn.datingClassTest()
trainingFileList = listdir('trainingDigits')
testvector = knn.img2vector('trainingDigits/%s' %trainingFileList)

print testvector[0,0:31]
"""

knn.HandWritingClassTest()
