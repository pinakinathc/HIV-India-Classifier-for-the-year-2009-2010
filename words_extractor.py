import glob
import operator
import PorterStemmer #make sure that the file PorterStemmer is present in same dir
word_list = []
temp = {}
files = glob.glob("2009/*.txt")
files = files + glob.glob("2010/*.txt")
for file in files:
	with open(file,'r') as myFile:
		article = myFile.read()
		article = article.split()
		for word in article:
			word = word.lower()
			if word not in temp:
				temp[word] = 1
			else:
				temp[word] = temp[word] + 1

temp1 = temp.items()
word_list = ''
for i in temp1:
#here we consider only those words that occur atleast 7 times
	if i[1]>=3:
		word_list = word_list + i[0]+' '

word_list = word_list[:len(word_list)-1]
word_list = PorterStemmer.access(word_list)

temp = word_list
temp = temp.split()
word_list = []
for i in temp:
	if i not in word_list:
		word_list.append(i)

output = ' '.join(word_list)
with open('list_of_words.txt','wb') as f:
	f.write(output)
	f.closed