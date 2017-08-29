
# coding: utf-8

# In[59]:

from string import punctuation




f2 = open("F:\\study\IP\\sangoshthi_content_curation-master\\stopwords.txt", "r",encoding="utf8") 
#f1 = open("F:\\study\\IP\\human_transcript\\QA43_human_transcript.txt", "r",encoding='utf8') 
#f1 = open("F:/study/IP/audioprocessing/QA44_87/QA/audio_87.txt", "r",encoding='utf8') 
f1 = open("F:\\study\\IP\\audioprocessing\\Consilidated_transcripts\\temperature_control.txt", "r",encoding='utf8') 


# In[60]:

file1_raw = f1.read()
file2_raw = f2.read()


# In[61]:

file1_words = file1_raw.split()
file2_words = file2_raw.split()


# In[62]:

print(file1_words)


# In[63]:

final_words=[]
for i in file1_words:
    if i not in file2_words:
        final_words.append(i)


# In[64]:

print(final_words)


# In[66]:

thefile = open('F:\\study\\IP\\audioprocessing\\Consilidated_transcripts\\temperature_control_without_stopword.txt', 'w',encoding='utf8')
thefile.write("\n".join(final_words).replace("\n"," "))
thefile.close()


# In[ ]:




# In[ ]:



