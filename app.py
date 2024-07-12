import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d793637456aa4f1d2eccff83bdb475de&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def recommend(movie):
   movie_index = movies[movies['title'] == movie].index[0]
   distances = similarity[movie_index]
   movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
   recommended_movies = []
   recommended_movies_posters = []
   for i in movies_list:
      movie_id = movies.iloc[i[0]].movie_id
      recommended_movies.append(movies.iloc[i[0]].title)
      recommended_movies_posters.append(fetch_poster(movie_id))
   return recommended_movies,recommended_movies_posters
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
   "Enter a movie.....",
   movies['title'].values,
   index=None,
   placeholder="Select a movie...",
)

if st.button("Recommend",type="primary"):
   names,posters = recommend(selected_movie_name)
   col1, col2, col3, col4, col5 = st.columns(5)

   with col1:
      st.write(names[0])
      st.image(posters[0],width=150)
   with col2:
      st.write(names[1])
      st.image(posters[1],width=150)
   with col3:
      st.write(names[2])
      st.image(posters[2],width=150)
   with col4:
      st.write(names[3])
      st.image(posters[3],width=150)
   with col5:
      st.write(names[4])
      st.image(posters[4],width=150)
