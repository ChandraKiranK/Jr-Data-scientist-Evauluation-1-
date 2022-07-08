#!/usr/bin/env python
# coding: utf-8

# In[1]:

'/home/appuser/venv/bin/python -m pip install --upgrade pip'
import pandas as pd
import re
import sys
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('vader_lexicon')

# In[2]:


st.markdown("<h1 style='text-align: center; color: white;'>Mismatched Reviews</h1>", unsafe_allow_html=True)


# In[3]:


stop_words =set(stopwords.words('english'))
stop_words.remove('not')
stop_words.remove('no')
lemmatizer = WordNetLemmatizer()
sentiment_analyzer = SentimentIntensityAnalyzer()


# In[4]:


def clean_data(df):
    clean_text = []
    for text in df.Text:
        text = re.sub(r'[^\w\s]','',str(text))
        text = re.sub(r'\d','',text)
        text_token = word_tokenize(text.lower().strip())
        text_no_stopwords = []
        for token in text_token:
            if token not in stop_words:
                token = lemmatizer.lemmatize(token)
                text_no_stopwords.append(token)
        clean_text.append(' '.join(text_no_stopwords))
    df['clean_text'] = clean_text
    return df


# In[5]:


def extract_star12(df):
    df1 = df[(df.Star == 1)] # 1 star 
    df2 = df[(df.Star == 2)] # 2 star
    df_final = pd.concat([df1,df2]) # 1 and 2 star
    return df_final


# In[6]:


def Sentiment_score(df_final):
    sent = []
    for i in df_final.clean_text:
        score = sentiment_analyzer.polarity_scores(i)
        if score['pos'] > 0.6:
            sent.append('Positive')
        else:
            sent.append('Neutral/Negative')
    df_final['sentiment'] = sent
    df_final.drop('clean_text',axis =1, inplace=True)
    return df_final


# In[7]:


def postive_star12(df_final):
    postive_12star = df_final[df_final.sentiment == 'Positive']
    return postive_12star


# In[8]:


st.write("There are times when a user writes Good, Nice App or any other positive text, in the review and gives negative rating. Goal is to identify such ratings where review text is good, but rating is negative")


# In[9]:


input_file  = st.file_uploader("Upload a CSV File",type=['csv'])


# In[10]:


if (input_file is not None) and input_file.name.endswith(".csv"):
    df = pd.read_csv(input_file, encoding = 'ISO-8859-1')
    try:
        df = clean_data(df)
        df_final = extract_star12(df)
        df_final = Sentiment_score(df_final)
        postive_12star = postive_star12(df_final)
        output = postive_12star[['ID','User Name','Text','Star','Thumbs Up']]
        st.caption("Ratings where review text is good, but rating is negative")
        st.dataframe(data= output,width=1000, height=500)
    except:
        st.markdown("<h2 style='text-align: center; color: red;'>Data format is not mathcing !!!</h2>", unsafe_allow_html=True)


# In[ ]:




