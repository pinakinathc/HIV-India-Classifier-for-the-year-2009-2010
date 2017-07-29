import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import glob
import helper


files = glob.glob('toi/2009/*.txt')
files += glob.glob('toi/2010/*.txt')
files += glob.glob('hindu/2009/*.txt')
files += glob.glob('hindu/2010/*.txt')

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
alpha = 0.001
print "Current value of aplha for MultinomialNB is: ",alpha

#uncomment the following for multi-class classification
total_accuracy = 0
for i in xrange(7):
	print "Shape of training vector: ",vector_train.shape
	print "Shape of training target: ",target_train[:,i].shape
	print "Shape of testing vector: ",vector_test.shape
	print "training target: \n",target_train[:,i]
	print "Testing target: \n",target_test[:,i]
	clf = MultinomialNB(alpha = alpha)
	clf.fit(vector_train,target_train[:,i])
	pred = clf.predict(vector_test)
	accuracy = (pred==target_test[:,i]).sum()*1.0/target_test.shape[0]*100
	total_accuracy += accuracy
	print "accuracy for class",i+1,": ", accuracy


	
	with open('data_generator.pickle', 'rb') as f:
		temp = pickle.load(f)
		f.closed

	pred_data = (clf.predict(vectorizer.transform(temp['article'])))

	for x,y in enumerate(pred_data):
		temp['target'][x].append(y)
		#print temp['target'][x]

	with open('data_generator.pickle', 'wb') as f:
		pickle.dump(temp, f, pickle.HIGHEST_PROTOCOL)
		f.closed



print "Total average accuracy: ",total_accuracy/7.0


#the following does classification multi-class classification but
#an article belonging to 'awareness-finance' is treated different from 'awareness' or 'finance'

# clf = MultinomialNB(alpha = alpha)
# clf.fit(vector_train,target_train)
# pred = clf.predict(vector_test)
# print "accuracy : ",(pred==target_test).sum()*1.0/target_test.shape[0]*100