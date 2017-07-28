Please clone this repository and run `python main.py` for execution.
Programming details are present at the end of this README.md file

The following few are some conventions that I followed to make this classifier multiclass and for ease of data storage.

For classification of articles according to various classes we use the trick of conversion of binary data to demical data:

Imagine the following binary data: 1010110

this means that the article is about (from left to right):
1. Awareness
2. Drugs
3. Finance
4. Future Prospects
5. Legal
6. Statistics
7. Stigma

conversion of binary data to decimal follows the following order for reason of simplicity in calculation:

decimal = 1*(2^0) + 0*(2^1) + 1*(2^2) + 0*(2^3) + 1*(2^4) + 1*(2^5) + 0*(2^6)

To represent the state of an article, we have state codes:
State Codes:
Andaman and nicobar island: 01
andhra pradesh: 02
arunanchal pradesh: 03
assam: 04
bihar: 05
chandighar: 06
chattisgarh: 07
daman and diu: 08
delhi: 09
goa: 10
gujarat: 11
haryana: 12
himachal pradesh: 13
jammu and kashmir: 14
jharkhand: 15
karnataka: 16
kerala: 17
madhya pradesh: 18
maharashtra: 19
manipur: 20
meghalaya: 21
mizoram: 22
nagaland: 23
odisha: 24
punducherry: 25
punjab: 26
rajasthan: 27
sikkim: 28
tamil nadu: 29
telegana: 30
tripura: 31
uttar pradesh: 32
uttarakhand: 33
west bangal: 34
others: 35

Format of the data:

The data is present in the form of a dictionary in .pickle format with the following format:

data = {'article':[...], 'article_publisher':[...], 'article_year':[...], 'article_state':[...], 'target':[...] } 





The following are programming details and may not be of much interest to general users:

1. Classification Algorithm Used: Multinomial Naive Baye's with value of alpha=0.007
2. Feature Extractor Used: TF-IDF
3. Port Stemmer (optional): Porter, 1980, An algorithm for suffix stripping, Program, Vol. 14, no. 3, pp 130-137;
Link: http://www.tartarus.org/~martin/PorterStemmer

The above Port Stemmer has been modified by me for application in this project.

4. Additional Feature Extractor provided in this repository: words_extractor.py

developed by me for use as the list of words helping in generating the future feature vector to be used by Naive Bayes Classifier

5. Library Used for Multinomial Naive Bayes implementation: scikit

6. List of words to do the manual classification, for training the classifier and testing accurary:

curl "https://api.datamuse.com/words?ml=text+to+be+fetched&max=1000" > output_file.json

this command is taken from: http://www.datamuse.com/api/

7. Finally The accuracy after running this script is: 80.5970149254