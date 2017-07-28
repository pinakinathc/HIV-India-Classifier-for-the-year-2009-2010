import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

raw = {}
with open('data.pickle','rb') as f:
	raw = pickle.load(f)
	f.closed

data = np.array(raw['article'])
target = np.array(raw['target'])

n = data.shape[0]
n1 = 4*n/5
print "Amount of training data: ",n1
print "Amount of testing data: ",(n-n1)
data_train = data[:n1]
data_test = data[n1:]
target_train = target[:n1]
target_test = target[n1:]

vectorizer = TfidfVectorizer()
vector_train = vectorizer.fit_transform(data_train)
vector_test = vectorizer.transform(data_test)

#you can choose to enter the value of alpha by hard-coding or during execution

#alpha = float(raw_input('Enter the value of alpha for MultinomialNB: '))
alpha = 0.007
print "Current value of aplha for MultinomialNB is: ",alpha

#uncomment the following for multi-class classification

#for i in xrange(7):
	# print vector_train.shape
	# print target_train[:,i].shape
	# print vector_test.shape
	# print target_train[:,i]
	# print target_test[:,i]
	# clf = MultinomialNB(alpha = alpha)
	# clf.fit(vector_train,target_train[:,i])
	# pred = clf.predict(vector_test[:,i])
	# print "accuracy for class",i+1,": ",(pred==target_test[:,i]).sum()*1.0/target_test.shape[0]*100


#the following does classification multi-class classification but
#an article belonging to 'awareness-finance' is treated different from 'awareness' or 'finance'

clf = MultinomialNB(alpha = alpha)
clf.fit(vector_train,target_train)
pred = clf.predict(vector_test)
print "accuracy : ",(pred==target_test).sum()*1.0/target_test.shape[0]*100