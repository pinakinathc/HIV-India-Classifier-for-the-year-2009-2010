import pickle
import glob

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


data = {'article':[],
 'article_publisher':[],
  'article_year':[],
   'article_state':[],
    'target':[] } 


for file in files:
	with open(file, 'r') as f:
		article = f.read()
		state = find_state(article)

		if state=='':
			continue

		if (article.strip()==''):
			continue

		target = []

		data['article'].append(article)
		if 'toi' in file: data['article_publisher'].append('toi')
		if 'hindu' in file: data['article_publisher'].append('hindu')
		if '2009' in file: data['article_year'].append('2009')
		if '2010' in file: data['article_year'].append('2010')
		data['article_state'].append(state)
		data['target'].append(target)

with open('data_generator.pickle','wb') as f:
	pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
	f.closed