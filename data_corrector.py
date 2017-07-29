import pickle
temp = {}

with open('data.pickle', 'rb') as f:
	temp = pickle.load(f)
	f.closed

for i, var in enumerate(temp['article']):
	if len(var)!=7:
		del temp['article'][i]
		del temp['article_publisher'][i]
		del temp['article_year'][i]
		del temp['article_state'][i]
		del temp['target'][i]

with open('data.pickle', 'wb') as f:
	pickle.dump(temp, f, pickle.HIGHEST_PROTOCOL)
	f.closed