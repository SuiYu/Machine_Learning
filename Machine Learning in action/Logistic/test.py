import logRegres
import logRegres1
from numpy import*  

dataArr , labelMat = logRegres.loadDataSet()
weight=logRegres.gradAscent(dataArr,labelMat)
#logRegres.plotBestFit(weight.getA())

weight = logRegres.stocGradAscent1(array(dataArr),labelMat)
#logRegres.plotBestFit(weight)
print logRegres.multiTest()