import pickle
import glob
import math

files = glob.glob('toi/2009/*.txt')
files += glob.glob('toi/2010/*.txt')
files += glob.glob('hindu/2009/*.txt')
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
#		print article
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

		target = math.pow(2,max((v,i) for i, v in enumerate(temp))[1])
		if target==0:
			continue
		data['article'].append(article)
		if 'toi' in file: data['article_publisher'].append('toi')
		if 'hindu' in file: data['article_publisher'].append('hindu')
		if '2009' in file: data['article_year'].append('2009')
		if '2010' in file: data['article_year'].append('2010')
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