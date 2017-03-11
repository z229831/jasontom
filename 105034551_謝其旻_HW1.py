import nltk
import string
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import io
import sys
import re
import codecs
from collections import Counter
import os
import csv




stopwords = set(stopwords.words('english'))
z = string.punctuation
#symbols and count
for symbol in z:
    stopwords.add(symbol)
    stopwords.update(z)
    stopwords.add("--")
    stopwords.add("'s")
    stopwords.add("'ve")
    stopwords.add("'re")
    stopwords.add("n't")
    stopwords.add("``")
    stopwords.add(".")
    stopwords.add("?")

pathProg = 'C:\\Users\\user\\Desktop\\textmining\\' #路徑導入
os.chdir(pathProg)
#line
file = open(pathProg +'/building_global_community.txt')
tt = file.read()
print(tt)
#normalize
tt = tt.lower()
print(tt)

#stopwords
e = word_tokenize(tt)
e=[a for a in e if a not in stopwords]
print (e)
#part of speech
nltk.pos_tag(e)
for sent in nltk.pos_tag_sents(word_tokenize(sent) for sent in e):
    print(' '.join('{0}/{1}'.format(word, pos) for word, pos in sent))



f1 = open(pathProg + 'count.csv', 'w')
w = csv.writer(f1,lineterminator='\n')


counter =Counter(e)
e = counter.most_common()
print(e)

with open('count.csv','w') as csvfile:
    name=['word','count']
    writer=csv.DictWriter(csvfile, fieldnames=name)

    writer.writeheader()
    for word, count in e:
       writer.writerow({'word':word,'count':count})




