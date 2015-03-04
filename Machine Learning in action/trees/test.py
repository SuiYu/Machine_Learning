import Tree
import treePlotter

"""
print myDat
print Tree.calcShannonEnt(myDat)
print Tree.splitDataSet(myDat,0,1)
print Tree.splitDataSet(myDat,0,0)
print Tree.chooseBestFeatureToSplit(myDat)
"""

"""
myTree = Tree.createTree(myDat,labels)
print myTree
"""
"""
treePlotter.creatPlot()
"""

"""
print treePlotter.getNumLeafs(myTree)
print  treePlotter.getTreeDepth(myTree)
treePlotter.creatPlot(myTree)
"""
"""
myDat,labels = Tree.createDataSet()
myTree = treePlotter.retrieveTree(0)
print myTree
print labels
print myDat
print Tree.classify(myTree,labels,[1,0])
print Tree.classify(myTree,labels,[1,1])
"""

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age' , 'prescript' , 'astigmatic' , 'tearRate']
lensesTree = Tree.createTree(lenses,lensesLabels)
treePlotter.creatPlot(lensesTree)