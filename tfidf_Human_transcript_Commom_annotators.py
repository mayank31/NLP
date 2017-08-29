
# coding: utf-8

# In[1]:

import gensim
from gensim import corpora, models,  similarities
import xlwt
from itertools import chain
import lda
import lda.datasets
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
from collections import Counter


# In[7]:

with open("F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\common_keywords_annotators.txt", encoding="utf8",errors='ignore') as f:
    lines = f.readlines()
for word in lines:
    print(word)
    print()
#print(lines)


# In[58]:

texts = []
correct_lines=[]
count_total_words=[]
import re
with open("F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\common_keywords_annotators.txt", encoding="utf8") as f:
    lines = f.readlines()
#lines = list(map(lambda s: s.strip(), lines))
for word in lines:
    correct_lines=[]
    #print(word)
    #word = list(map(lambda s: s.strip('\t'), word))
    word=word.split(" ")
    #print(word)
    for i in word:
        #print(i)
        if i is not "" and i is not "\n":
            i=i.split("\t")
            
                    
            #j = re.sub('[@#$"()“”\n]', '', j)
            print(i)
            for j in i:
                
                count_total_words.append(j)
                correct_lines.append(j)
    texts.append(correct_lines)

len_words=len(count_total_words)
count = Counter(count_total_words)
print(count)


# In[60]:

import math
import codecs
import textblob
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    
    return math.log(len(bloblist) / (n_containing(word, bloblist)),2)
print(len(texts))
file = open("F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA1_QA43_tfidf_results_maual_data.txt", "w",encoding="utf8")

for i in count.most_common(len(count)):
    tf=i[1]/len_words
    idf1=idf(i[0],texts)
    #print(tf,idf1)
    tfidf_words=tf*idf1
    file.write(i[0])
    file.write('\t')
    file.write(str(tfidf_words))
    file.write('\n')
    print(i,tfidf_words)
file.close()


# In[ ]:



