
# coding: utf-8

# In[6]:

import math
import codecs
import textblob


from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    #print((1 + n_containing(word, bloblist)))
    value=math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
    #print(value)
    return value

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


# In[2]:

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA1_nouns.txt",'r',encoding='utf8') as f:
    document1 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA2_nouns.txt",'r',encoding='utf8') as f:
    document2 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA3_nouns.txt",'r',encoding='utf8') as f:
    document3 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA4_nouns.txt",'r',encoding='utf8') as f:
    document4 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_5_nouns.txt",'r',encoding='utf8') as f:
    document5 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_6_nouns.txt",'r',encoding='utf8') as f:
    document6 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_7_nouns.txt",'r',encoding='utf8') as f:
    document7 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_8_nouns.txt",'r',encoding='utf8') as f:
    document8 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_9_nouns.txt",'r',encoding='utf8') as f:
    document9 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_10_nouns.txt",'r',encoding='utf8') as f:
    document10 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_11_nouns.txt",'r',encoding='utf8') as f:
    document11 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_13_nouns.txt",'r',encoding='utf8') as f:
    document13 = tb(f.read())
	
with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_14_nouns.txt",'r',encoding='utf8') as f:
    document14 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_15_nouns.txt",'r',encoding='utf8') as f:
    document15 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_16_nouns.txt",'r',encoding='utf8') as f:
    document16 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_17_nouns.txt",'r',encoding='utf8') as f:
    document17 = tb(f.read())
	
with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_18_nouns.txt",'r',encoding='utf8') as f:
    document18 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_19_nouns.txt",'r',encoding='utf8') as f:
    document19 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_20_nouns.txt",'r',encoding='utf8') as f:
    document20 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\audio_21_nouns.txt",'r',encoding='utf8') as f:
    document21 = tb(f.read())
    
with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA23_nouns.txt",'r',encoding='utf8') as f:
    document23 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA24_nouns.txt",'r',encoding='utf8') as f:
    document24 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA25_nouns.txt",'r',encoding='utf8') as f:
    document25 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA26_nouns.txt",'r',encoding='utf8') as f:
    document26 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA27_nouns.txt",'r',encoding='utf8') as f:
    document27 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA28_nouns.txt",'r',encoding='utf8') as f:
    document28 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA29_nouns.txt",'r',encoding='utf8') as f:
    document29 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA30_nouns.txt",'r',encoding='utf8') as f:
    document30 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA31_nouns.txt",'r',encoding='utf8') as f:
    document31 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA32_nouns.txt",'r',encoding='utf8') as f:
    document32= tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA33_nouns.txt",'r',encoding='utf8') as f:
    document33 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA34_nouns.txt",'r',encoding='utf8') as f:
    document34 = tb(f.read())
    
with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA35_nouns.txt",'r',encoding='utf8') as f:
    document35 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA36_nouns.txt",'r',encoding='utf8') as f:
    document36 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA37_nouns.txt",'r',encoding='utf8') as f:
    document37 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA38_nouns.txt",'r',encoding='utf8') as f:
    document38 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA39_nouns.txt",'r',encoding='utf8') as f:
    document39 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA40_nouns.txt",'r',encoding='utf8') as f:
    document40 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA41_nouns.txt",'r',encoding='utf8') as f:
    document41 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA42_nouns.txt",'r',encoding='utf8') as f:
    document42 = tb(f.read())

with codecs.open("F:\\study\\IP\\audioprocessing\\POS_tagged\\QA43_nouns.txt",'r',encoding='utf8') as f:
    document43 = tb(f.read())


# In[7]:

file = open("F:\\study\\IP\\audioprocessing\\POS_tagged\\result_tf_idf_keyword.txt", "w",encoding="utf8")
bloblist = [document1,document2,document3,document4,document5, document6, document7,document8,document9, document10, document11,document13,document14, document15, document16,document17,document18, document19, document20,document21,document23,document24,document25,document26,document27, document28, document29,document30,document31, document32, document33,document34,document35, document36, document37,document38,document39, document40, document41,document42,document43]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    file.write("Top words in document {}".format(i + 1))
    file.write("\n")
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    #print(scores)
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        file.write("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        file.write("\n")
file.close()


# In[9]:

"""file = open("F:\\study\\IP\\audioprocessing\\POS_tagged\\result_tf_idf_LDA_keyword.txt", "w",encoding="utf8")
bloblist = [document1,document2,document3,document4,document5, document6, document7,document8,document9, document10, document11,document13,document14, document15, document16,document17,document18, document19, document20,document21,document23,document24,document25,document26,document27, document28, document29,document30,document31, document32, document33,document34,document35, document36, document37,document38,document39, document40, document41,document42,document43]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    file.write("Top words in document {}".format(i + 1))
    file.write("\n")
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        file.write("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        file.write("\n")
file.close()
"""


# In[ ]:



