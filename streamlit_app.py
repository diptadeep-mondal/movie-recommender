import streamlit as st
import pickle
import pandas as pd
st.title('movie recommendation system')
df=pickle.load(open('movie_list.plk','rb'))
similarity=pickle.load(open('similarity.plk','rb'))
def recommend(movie):
    movie_index=df[df['original_title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    for i in movies_list:
        l.append(df.iloc[i[0]].original_title)
    return  l

movies_list=df['original_title']

option = st.selectbox("which movie you like",movies_list)
if st.button('recommend'):
    re=recommend(option)
    for i in re:
        st.write(i)
