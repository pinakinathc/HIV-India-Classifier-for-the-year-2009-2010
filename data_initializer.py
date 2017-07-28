import pickle

data = {'article':[],
'article_publisher':[],
'article_year':[],
'article_state':[], 
'target':[] }
with open('data.pickle', 'wb') as f:
	pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
	f.closed