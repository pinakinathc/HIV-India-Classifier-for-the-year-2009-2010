import pickle
temp = {}

with open('data.pickle', 'rb') as f:
	temp = pickle.load(f)
	f.closed

counter = 0

for i, var in enumerate(temp['target']):
	if len(var)!=7:
		counter += 1
		#print "index and target: ",i, var
		del temp['article'][i]
		del temp['article_publisher'][i]
		del temp['article_year'][i]
		del temp['article_state'][i]
		del temp['target'][i]

#print "No of entries deleted due to wrong target values: ",counter

with open('data.pickle', 'wb') as f:
	pickle.dump(temp, f, pickle.HIGHEST_PROTOCOL)
	f.closed