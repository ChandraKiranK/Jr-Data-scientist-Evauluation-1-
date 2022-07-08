#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem import WordNetLemmatizer 
from textblob import TextBlob
lemmatizer = WordNetLemmatizer()


# In[2]:


data = pd.read_csv('chrome_reviews.csv')
data.head()


# In[3]:


data.info()


# In[4]:


data_star1 = data[data['Star']==1]


# In[5]:


data_star1


# In[6]:


data_star1.info()


# In[7]:


stop_words = set(stopwords.words('english'))
stop_words.remove('not')
stop_words.remove('no')


# In[15]:


clean_text = []
for text in data_star1['Text']:
    text = re.sub(r'[^\w\s]','', str(text))
    text = re.sub(r'\d','', text)
    text_token = word_tokenize(text.lower().strip())
    text_stopwords = []
    for token in text_token:
        if token not in stop_words:
            token=lemmatizer.lemmatize(token)
            text_stopwords.append(token)
    text_join = " ".join(text_stopwords)
    clean_text.append(text_join)
            


# In[14]:


data_star1['cleaned_text'] = clean_text


# In[27]:


senti_list = []
sia = SentimentIntensityAnalyzer()
for i in data_star1['cleaned_text']:
    score = sia.polarity_scores(i)
    if (score['pos']>=0.7):
        senti_list.append('Positive')
    else:
        senti_list.append('Negative/Neutral')
data_star1['Sentiment'] = senti_list


# In[30]:


data_star1['Sentiment'].value_counts()


# In[36]:


PosReview_rating1 = data_star1[data_star1['Sentiment']=='Positive']
PosReview_rating1.head()


# In[ ]:




