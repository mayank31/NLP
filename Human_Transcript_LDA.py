
# coding: utf-8

# In[ ]:

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


# In[ ]:

#doc1="F:\\study\\IP\\audioprocessing\\POS_tagged\\QA1_nouns.txt";
doc2="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA2_human_transcripts_POS_nouns.txt";
doc3="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA3_human_transcripts_POS_nouns.txt";
doc4="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA4_human_transcripts_POS_nouns.txt";
doc5="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA5_human_transcripts_POS_nouns.txt";
doc6="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA6_human_transcripts_POS_nouns.txt";
doc7="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA7_human_transcripts_POS_nouns.txt";
doc8="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA8_human_transcripts_POS_nouns.txt";
doc9="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA9_human_transcripts_POS_nouns.txt";
doc10="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA10_human_transcripts_POS_nouns.txt";
doc11="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA11_human_transcripts_POS_nouns.txt";
#doc12="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA12_human_transcripts_POS_nouns.txt";
doc13="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA13_human_transcripts_POS_nouns.txt";
doc14="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA14_human_transcripts_POS_nouns.txt";
doc15="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA15_human_transcripts_POS_nouns.txt";
doc16="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA16_human_transcripts_POS_nouns.txt";
doc17="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA17_human_transcripts_POS_nouns.txt";
doc18="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA18_human_transcripts_POS_nouns.txt";
doc19="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA19_human_transcripts_POS_nouns.txt";
doc20="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA20_human_transcripts_POS_nouns.txt";
doc21="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA22_human_transcripts_POS_nouns.txt";
doc22="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA21_human_transcripts_POS_nouns.txt";
doc23="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA23_human_transcripts_POS_nouns.txt";
doc24="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA24_human_transcripts_POS_nouns.txt";
doc25="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA25_human_transcripts_POS_nouns.txt";
doc26="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA26_human_transcripts_POS_nouns.txt";
doc27="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA27_human_transcripts_POS_nouns.txt";
doc28="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA28_human_transcripts_POS_nouns.txt";
doc29="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA29_human_transcripts_POS_nouns.txt";
doc30="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA30_human_transcripts_POS_nouns.txt";
#doc31="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA31_human_transcripts_POS_nouns.txt";
doc32="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA32_human_transcripts_POS_nouns.txt";
doc33="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA33_human_transcripts_POS_nouns.txt";
doc34="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA34_human_transcripts_POS_nouns.txt";
doc35="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA35_human_transcripts_POS_nouns.txt";
doc36="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA36_human_transcripts_POS_nouns.txt";
doc37="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA37_human_transcripts_POS_nouns.txt";
doc38="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA38_human_transcripts_POS_nouns.txt";
doc39="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA39_human_transcripts_POS_nouns.txt";
doc40="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA40_human_transcripts_POS_nouns.txt";
doc41="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA41_human_transcripts_POS_nouns.txt";
doc42="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA42_human_transcripts_POS_nouns.txt";
doc43="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA43_human_transcripts_POS_nouns.txt";


# In[ ]:

doc_set = [doc2,doc3,doc4,doc5, doc6, doc7, doc8, doc9,doc10, doc11, doc13, doc14, doc15,doc16, doc17, doc18, doc19, doc20,doc21,doc22,doc23,doc24,doc25,doc26,doc27, doc28, doc29, doc30,doc32, doc33, doc34, doc35, doc36,doc37, doc38, doc39, doc40, doc41,doc42,doc43]


# In[ ]:

file_remove_words="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA1_QA43_irrelevant_words_tfidf.txt"
w1=[]
with open(file_remove_words,encoding="utf8") as f:
    w1=f.readlines()
w1=list(map(lambda s:s.strip(),w1))
w1.append("बच्चा")
print(w1)


# In[ ]:

texts = []
correct_lines=[]

for i in doc_set:
    with open(i, encoding="utf8") as f:
        lines = f.readlines()
    lines = list(map(lambda s: s.strip(), lines))
    correct_lines=[]
    for j in lines:
        
        if j not in w1:
            
            correct_lines.append(j)
    texts.append(correct_lines)
#texts.append(count_total_words)


# In[ ]:

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=12, id2word = dictionary,chunksize=5000, passes=50)


# In[ ]:

lda_corpus = ldamodel[corpus]
#print(len(lda_corpus))
index = similarities.MatrixSimilarity(ldamodel[corpus])
#print(index)
sims = index[lda_corpus]
#print(list(enumerate(sims)))
# Find the threshold, let's set the threshold to be 1/#clusters,
# To prove that the threshold is sane, we average the sum of all probabilities:
scores = list(chain(*[[score for topic_id,score in topic] 
                     for topic in [doc for doc in lda_corpus]]))
reverse_map = dict((ldamodel.id2word[id],id) for id in ldamodel.id2word)
threshold = sum(scores)/len(scores)


# In[ ]:

file = open("F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\Human_results_LDA_words4_passes50_topics12_relevant.txt", "w",encoding="utf8")
#file = open("F:\\study\\IP\\audioprocessing\\POS_tagged\\results_LDA_words10_passes50_topics10_updated.txt", "w",encoding="utf8")
l=list(map(str,(ldamodel.print_topics(num_topics=12, num_words=4))))
for i in l:
    file.write(i)
    file.write("\n")
file.close()
file = open("F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\Human_results_LDA_words4_passes50_topics12_relevant_mapping.txt", "w",encoding="utf8")
for i,j in zip(lda_corpus,doc_set):
    for k in i:
        for m in k:
            file.write(str(m))
            file.write("\t")
        #file.write(k)
    
    file.write(j)
    file.write("\n")
file.close()


# In[ ]:




# In[ ]:



