#This file is for manually classifying the entire data
#Please remember that once you start labelling data, you must either
#label all the data(which can be pretty difficult given the size of data)
#or input '-1' in the field of data for state to stop taking anymore data from files.



import pickle
import glob
import math
import os

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
files += glob.glob('hindu/2009/*.txt')
files += glob.glob('hindu/2010/*.txt')

data = {}

counter = 0;

for file in files:
	with open('data.pickle','rb') as d:
		data = pickle.load(d)
		d.closed
	with open(file, 'r') as f:

		#This is done to begin labeling data from where i left
		if (counter<80):
			counter += 1
			continue
		# print "File now coming: ",file
		# inp = input()
		article = f.read()
		if (article.strip() == ''):
			continue
		state = find_state(article)
		if state=='':
			continue

		print article
		
		print "\n\n\n"
		print "State: ",state
		signal = int(raw_input('Enter 0 to reject data and -1 to stop else press any other number: '))
		print
		target = map(int,raw_input("Please Enter the Classification bits: ").split())
		# target = 0
		# for i,p in enumerate(temp):
		# 	target += int(p*(math.pow(2,i)))
		# print "setting target value: ",target
#enter value of state as 0 if you want to ignore that article
		if signal == 0:
			continue
#enter the value of state -1 if you want to stop taking any more data from the files
		if signal == -1:
			break
		data['article_state'].append(state)
		data['target'].append(target)
		data['article'].append(article)
		if 'toi' in file: data['article_publisher'].append('toi')
		if 'hindu' in file: data['article_publisher'].append('hindu')
		if '2009' in file: data['article_year'].append('2009')
		if '2010' in file: data['article_year'].append('2010')
		counter += 1
		print "Counter = ",counter
		print "\n\n\n"

	os.system('python data_initializer.py') #cleans data before storing new data
	with open('data.pickle','wb') as f:
		pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
		f.closed