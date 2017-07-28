#This file is for manually classifying the entire data
#Please remember that once you start labelling data, you must either
#label all the data(which can be pretty difficult given the size of data)
#or input '-1' in the field of data for state to stop taking anymore data from files.



import pickle
import glob
import math

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
		article = f.read()
		if (article == ''):
			continue
		print article
		
		print "\n\n\n"
		state = int(raw_input('Enter the Sate Code for article or 0 to reject data: '))
		print
		temp = map(int,raw_input("Please Enter the Classification bits: ").split())
		target = 0
		for i,p in enumerate(temp):
			target += int(p*(math.pow(2,i)))
		print "setting target value: ",target
#enter value of state as 0 if you want to ignore that article
		if state == 0:
			continue
#enter the value of state -1 if you want to stop taking any more data from the files
		if state == -1:
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

	with open('data.pickle','wb') as f:
		pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
		f.closed