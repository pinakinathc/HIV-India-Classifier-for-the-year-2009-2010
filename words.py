#This file takes all the words present in the directory 'classes' and creates
#a list of words to be used for feature extraction manually.


import json
import pickle
words = {'awareness':['awareness'], 'drugs':['drugs'], 'finance':['finance'],
'future_prospects':['future_prospects'], 'legal':['legal'],
 'statistics':['statistics'], 'stigma':['stigma']}

classes = ['awareness','drugs','finance',
'future_prospects', 'legal',
'statistics', 'stigma']

for cl in classes:
	with open('classes/'+cl+'.json') as j:
		temp = json.load(j)
		for t in temp:
			arr = t['word'].encode('utf8').split()
			for a in arr:
				words[cl].append(a)

with open('words.pickle', 'wb') as f:
	pickle.dump(words, f, pickle.HIGHEST_PROTOCOL)
	f.closed