import pickle
import matplotlib.pyplot as plt
import numpy as np 

data = {}
with open('data_generator.pickle','rb') as f:
	data = pickle.load(f)
	f.closed

toi_2009 = 0
toi_2010 = 0
hindu_2009 = 0
hindu_2010 = 0
x = np.arange(2)
#plt.title('Total articles by year')

for i, j in enumerate(data['article_publisher']):
	if j=='toi':
		if (data['article_year'][i]=='2009'):
			toi_2009 += 1
		else:
			toi_2010 += 1
	else:
		if (data['article_year'][i]=='2009'):
			hindu_2009 += 1
		else:
			hindu_2010 += 1


plt.figure(1)
plt.subplot(121)
plt.bar(x,height=[toi_2009, toi_2010], color='green')
plt.xticks(x,['TOI 2009', 'TOI 2010'])
plt.title('Times of India')

plt.subplot(122)
plt.bar(x, height=[hindu_2009, hindu_2010])
plt.xticks(x,['HINDU 2009', 'HINDU 2010'])
plt.title('The Hindu')

#plt.figure(2)

state_dict = {}
state = []
for var in data['article_state']:
	if var not in state:
		state.append(var)
		state_dict[var] = [0 for i in xrange(7)]

state.sort()

for i, var in enumerate(data['target']):
	for j ,k in enumerate(var):
		state_dict[ data['article_state'][i] ][j] += k

plt.rcdefaults()
fig, ax = plt.subplots(1,7, sharey=True)
labl = ['awareness','drugs','finance','future_prospects','legal','statistics','stigma']
for i in xrange(7):
	#plt.subplot(1,7,i+1)
	y_pos = np.arange(len(state))
	cl =[]
	for st in state:
		cl.append(state_dict[st][i])
	ax[i].barh(y_pos, cl, align='center', color='green', ecolor='black')
	if i==0:
		ax[i].set_yticks(y_pos)

	ax[i].invert_yaxis()
	if i>0:
		ax[i].yaxis.set_visible(False)
	else:
		ax[i].set_yticklabels(state, minor=False)
	ax[i].set_title(labl[i])
	for j, v in enumerate(cl):
		ax[i].text(v,j,str(v))


# plt.rcdefaults()
# # fig, ax = plt.subplots()
# y_pos = np.arange(7)
# print len(y_pos)
# print len(state_dict[state[0]])
# plt.barh(y_pos, state_dict[state[0]])

plt.show()


