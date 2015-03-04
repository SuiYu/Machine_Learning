import bayes
import re
import feedparser
from numpy import *

"""
listOPost,listClasses = bayes.loadDataSet()
#print listClasses,listOPost
myVocabulary = bayes.creatVocabList(listOPost)
print myVocabulary
print bayes.setOfWords2Vec(myVocabulary,listOPost[1])

trainMat = []
for postinDoc in listOPost:
	trainMat.append(bayes.setOfWords2Vec(myVocabulary,postinDoc))

p0v,p1v,pAb = bayes.trainNB0(trainMat,listClasses) 
print p0v
print '\n',p1v
print '\n',pAb

"""
"""
print bayes.testingNB()


mySent = 'This is a nice book i never see on Pyhton of M.r. I like it very much.'

regEx = re.compile('\\W*')
ListOfTokens = regEx.split(mySent)
[tok for tok in ListOfTokens if len(tok)>0]
print ListOfTokens
"""

#bayes.spamTest()

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
print ny
ny['entries']
print len(ny['entries'])