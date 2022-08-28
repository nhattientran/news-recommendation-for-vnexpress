import streamlit as st
import pandas as pd
import numpy as np
from numpy import load


#Load matrix

w2v_similarity = load("w2v/w2v_similarity.npy")

dataset = pd.read_csv('data/vnexpress_news.csv')

user = pd.read_csv('data/test_set.csv')


mapping = pd.Series(dataset.index,index=dataset['NewsTitle'])


def get_newtitle(newsid):
  return dataset[dataset['NewsID']==newsid]['NewsTitle'].values[0]

def get_newid(newtitle):
  return dataset[dataset['NewsTitle']==newtitle]['NewsID'].values[0]

def recommend_news(userid,newid):
  title = get_newtitle(str(newid))
  new_index = mapping[title]
  similarity_score = list(enumerate(w2v_similarity[new_index]))
  similarity_score = sorted(similarity_score, key = lambda x:x[1],reverse=True)
  similarity_score = similarity_score[1:11]
  recommendations = [dataset['NewsTitle'].loc[index] for index,score in similarity_score]
  return recommendations

UserID = user['UserID']
userid = st.selectbox('User ID',UserID)
NewsID = user[user['UserID']==userid]['NewsID'].values[0].split()
Titles = [get_newtitle(id) for id in NewsID ]
title = st.selectbox('Title',Titles)
newid = get_newid(title)

recommendations = recommend_news(userid,newid)

for title in recommendations:
	st.write(title)
