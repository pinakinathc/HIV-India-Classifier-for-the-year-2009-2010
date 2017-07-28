#Please avoid this file, as it contains older version of the updated version
#of this file: semi_automated.py
#This file is kept for the sole purpose of future development.


import pickle
import glob
import math

files = glob.glob('toi/2009/*.txt')
files += glob.glob('toi/2010/*.txt')

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
		if (article==''):
			continue

		output = []
		word = ''

		for c in article:
			if c.isalpha():
				word += c.lower()
			else:
				if word:
					if word in words['awareness'][:500]: temp[0] += 1
					if word in words['drugs'][:500]: temp[1] += 1
					if word in words['finance'][:500]: temp[2] += 1
					if word in words['future_prospects'][:500]: temp[3] += 1
					if word in words['legal'][:500]: temp[4] += 1
					if word in words['statistics'][:500]: temp[5] += 1
					if word in words['stigma'][:500]: temp[6] += 1
					number_of_words += 1
					#print word
					#inp = input()
					word = ''

		#print words['awareness'][:500]
		#inp = input()

		#increase alpha to increase more resemblence of data to classes
		alpha = [6,1,7,7,14,10,7]
		target = []
		#target = [int(int(i*1.0/number_of_words*100)>alpha) for i in temp]
		for i in xrange(7):
			target.append( int(int(temp[i]*1.0/number_of_words*100)>alpha[i]) )
		print target
		# inp = input()


		data['article'].append(article)
		if 'toi' in file: data['article_publisher'].append('toi')
		if 'hindu' in file: data['article_publisher'].append('hindu')
		if '2009' in file: data['article_year'].append('2009')
		if '2010' in file: data['article_year'].append('2010')
		#data['article_state'] = raw_input('Enter the Sate Code for article: ')
		print
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