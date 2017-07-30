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

We classify for each of these classes seperately

States Listed in This Repository:

1. Andaman & Nicobar [AN]
2. Andhra Pradesh [AP]
3. Arunachal Pradesh [AR]
4. Assam [AS]
5. Bihar [BH]
6. Chandigarh [CH]
7. Chhattisgarh [CG]
8. Dadra & Nagar Haveli [DN]
9. Daman & Diu [DD]
10. Delhi [DL]
11. Goa [GO]
12. Gujarat [GU]
13. Haryana [HR]
14. Himachal Pradesh [HP]
15. Jammu & Kashmir [JK]
16. Jharkhand [JH]
17. Karnataka [KR]
18. Kerala [KL]
19. Lakshadweep [LD]
20. Madhya Pradesh [MP]
21. Maharashtra [MH]
22. Manipur [MN]
23. Meghalaya [ML]
24. Mizoram [MM]
25. Nagaland [NL]
26. Orissa [OR]
27. Pondicherry [PC]
28. Punjab [PJ]
29. Rajasthan [RJ]
30. Sikkim [SK]
31. Tamil Nadu [TN]
32. Tripura [TR]
33. Uttar Pradesh [UP]
34. Uttaranchal [UT]
35. West Bengal [WB]

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
   Library Used for Plotting Bar Graphs: Matplot

6. [Later has been opted out due to poor results] List of words to do the manual classification, for training the classifier and testing accurary:

curl "https://api.datamuse.com/words?ml=text+to+be+fetched&max=1000" > output_file.json

this command is taken from: http://www.datamuse.com/api/

7. Finally The accuracy after running this script is: ~ 80 %