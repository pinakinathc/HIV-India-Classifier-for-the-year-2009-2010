import pickle
import glob
import math
import operator
import PorterStemmer

def find_state(article):
	citi_data = {}
	word = ''
	with open('cities/citi_data.pickle', 'rb') as f:
		citi_data = pickle.load(f)
		f.closed

	for c in article:
			if c.isalpha():
				word += c.lower()
			else:
				if word:
					for name, var in citi_data.iteritems():
						if word in var:
							return name

					word = ''
	return ''
	

files = glob.glob('toi/2009/*.txt')
files += glob.glob('toi/2010/*.txt')
#files += glob.glob('hindu/2009/*.txt')
#note: uncommenting the following line may lead to memory overflow as it contains a lot of data which gets stored in the buffer.

#files += glob.glob('hindu/2010/*.txt')

words = {}
with open('words.pickle', 'rb') as f:
	words = pickle.load(f)
	f.closed
#print words

temp = [0 for i in xrange(7)]
number_of_words = 0;

data = {}
with open('data.pickle','rb') as d:
	data = pickle.load(d)
	d.closed

for file in files:
	with open(file, 'r') as f:
		article = f.read()
		state = find_state(article)

		if state=='':
			continue

		article = PorterStemmer.access(article)
		# print article
		# inp = input()
		if (article.strip()==''):
			continue

		output = []
		word = ''

		for c in article:
			if c.isalpha():
				word += c.lower()
			else:
				if word:
					if word in words['awareness']: temp[0] += 1
					if word in words['drugs']: temp[1] += 1
					if word in words['finance']: temp[2] += 1
					if word in words['future_prospects']: temp[3] += 1
					if word in words['legal']: temp[4] += 1
					if word in words['statistics']: temp[5] += 1
					if word in words['stigma']: temp[6] += 1
					number_of_words += 1


					word = ''

		target = [0 for i in xrange(7)]
		temp = [i*1.0/number_of_words*100 for i in temp]

#for multiclass-classification of the same data, use vector notation, given in the comment below

#		target[max((v,i) for i, v in enumerate(temp))[1]] = 1


		#taking the top 3 classes and making their bits equal to 1. Refer to README.md for this convention of classification
		temp_1 = [[i,j]	for i,j in enumerate(temp)]
		temp_1.sort(key=operator.itemgetter(1))
		target[temp_1[0][0]] = 1
		target[temp_1[1][0]] = 1
		target[temp_1[2][0]] = 1	

#		target = math.pow(2,max((v,i) for i, v in enumerate(temp))[1])


#Use the below of the target value of not an array, which is done for multi-class-classification
#		if target==0:
#			continue

		if target==[0 for i in xrange(7)]:
			continue


		data['article'].append(article)
		if 'toi' in file: data['article_publisher'].append('toi')
		if 'hindu' in file: data['article_publisher'].append('hindu')
		if '2009' in file: data['article_year'].append('2009')
		if '2010' in file: data['article_year'].append('2010')
		data['article_state'] = state
		#data['article_state'] = raw_input('Enter the Sate Code for article: ')
		#print
		#temp = map(int,raw_input("Please Enter the Classification bits: ").split())
		#target = 0
		#for i,p in enumerate(temp):
		#	target += int(p*(math.pow(2,i)))
		#print "setting target value: ",target
		data['target'].append(target)
		#print "\n\n\n"

with open('data.pickle','wb') as f:
	pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
	f.closed