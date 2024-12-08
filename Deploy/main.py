import streamlit as st
import pickle as pkl
import requests

def fetch_poster(movie_id):
    respond = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=20a43036439b337081d87a4b8695f553&language=en-US")
    data = respond.json()
    return 'https://image.tmdb.org/t/p/w185' + data['poster_path']

movies = pkl.load(open('movies.pkl', 'rb'))
movies_list = movies['title_x']
similarity = pkl.load(open('similarity.pkl', 'rb'))

def recommend(movie_name):
    movie_index = movies[movies_list == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse =True , key = lambda x:x[1])[1:6]
    recommed_movies = []
    recommed_movies_poster= []

    for i in movie_list:

        recommed_movies.append(movies.iloc[i[0]][1])

        #fetch poster
        poster=fetch_poster(movies.iloc[i[0]][0])

        recommed_movies_poster.append(poster)

    return recommed_movies, recommed_movies_poster


st.title("Movie Recommendation System")

select_movie_name = st.selectbox(
    "which movie do you like most?",movies_list)


if st.button("Recommend"):

    name, poster = recommend(select_movie_name)
    c1, c2, c3, c4, c5 = st.columns(5)
    col =[c1, c2, c3, c4, c5 ]
    for i, j, k in zip(name, poster, col):
        with k:
            st.text(i)
            st.image(j)
