
# coding: utf-8

# In[1]:

from collections import Counter


# In[5]:

doc1="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA1_nouns.txt";
doc2="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA2_nouns.txt";
doc3="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA3_nouns.txt";
doc4="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA4_nouns.txt";
doc5="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA5_nouns.txt";
doc6="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA6_nouns.txt";
doc7="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA7_nouns.txt";
doc8="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA8_nouns.txt";
doc9="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA9_nouns.txt";
doc10="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA10_nouns.txt";
doc11="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA11_nouns.txt";
doc13="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA13_nouns.txt";
doc14="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA14_nouns.txt";
doc15="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA15_nouns.txt";
doc16="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA16_nouns.txt";
doc17="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA17_nouns.txt";
doc18="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA18_nouns.txt";
doc19="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA19_nouns.txt";
doc20="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA20_nouns.txt";
doc21="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA21_nouns.txt";
#doc22="F:\\study\\IP\\human_transcript\\QA1_QA43_human_transcripts_POS_tagging\\QA21_human_transcripts_POS_nouns.txt";
doc23="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA23_nouns.txt";
doc24="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA24_nouns.txt";
doc25="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA25_nouns.txt";
doc26="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA26_nouns.txt";
doc27="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA27_nouns.txt";
doc28="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA28_nouns.txt";
doc29="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA29_nouns.txt";
doc30="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA30_nouns.txt";
doc31="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA31_nouns.txt";
doc32="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA32_nouns.txt";
doc33="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA33_nouns.txt";
doc34="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA34_nouns.txt";
doc35="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA35_nouns.txt";
doc36="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA36_nouns.txt";
doc37="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA37_nouns.txt";
doc38="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA38_nouns.txt";
doc39="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA39_nouns.txt";
doc40="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA40_nouns.txt";
doc41="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA41_nouns.txt";
doc42="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA42_nouns.txt";
doc43="F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_QA43_nouns.txt";


# In[6]:

doc_set = [doc1,doc2,doc3,doc4,doc5, doc6, doc7, doc8, doc9,doc10, doc11, doc13, doc14, doc15,doc16, doc17, doc18, doc19, doc20,doc21,doc23,doc24,doc25,doc26,doc27, doc28, doc29, doc30,doc31,doc32, doc33, doc34, doc35, doc36,doc37, doc38, doc39, doc40, doc41,doc42,doc43]


# In[30]:

texts = []
correct_lines=[]
#count_total_words=[]
for i in doc_set:
    with open(i, encoding="utf8") as f:
        lines = f.readlines()
    lines = list(map(lambda s: s.strip(), lines))
    
    for j in lines:
        if j is not "\ufeff":
        #count_total_words.append(j)   
            correct_lines.append(j)
texts.append(correct_lines)


# In[31]:

count = Counter(correct_lines)
print(count)


# In[32]:

file = open("F:\\study\\IP\\audioprocessing\\POS_tagged\\output\\ASR_most_frequent_words.txt", "w",encoding="utf8")
value=[]
value=count.values()
#print(texts)
#print(value)
j=0
for i in count.most_common(int(len(count)/10)):
    print(i)
    file.write(i[0])
    #print(count.get(i))
    #file.write("\t")
    #file.write(str(count.get(i)))
    #file.write(str(i[1]))
    j=j+1
    file.write("\n")
file.close()
print(j)
print(len(count))


# In[ ]:




# In[ ]:



