#this python code takes input from a text file `raw_data.txt` and converts it into
#dictionary stored in `citi_data.pickle` for later use in classifying articles
#according to which state in India, is it related to.

import pickle
with open('raw_data.txt','rb') as f:
	raw = f.readlines()
	f.closed

raw = [x.strip() for x in raw]
data = {}
last = ''
for i in raw:
	if i=='':
		continue
	if (i[0].isalpha()):
		last = i.split()
		last = ' '.join( last[:len(last)-1] ).lower()
		data[last] = []
	else:
		temp = ' '.join(i.split()[1:]).lower()
		data[last].append( temp )

with open('citi_data.pickle','wb') as f:
	pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
	f.closed