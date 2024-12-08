import streamlit as st
import pickle as pkl

movies = pkl.load(open('movies.pkl', 'rb'))
movies_list = movies['title_x']
similarity = pkl.load(open('similarity.pkl', 'rb'))

def recommend(movie_name):
    movie_index = movies[movies_list == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse =True , key = lambda x:x[1])[1:6]
    recommed_movies = []
    for i in movie_list:
        recommed_movies.append(movies.iloc[i[0]][1])
    return recommed_movies


st.title("Movie Recommendation System")

select_movie_name = st.selectbox(
    "which movie do you like most?",movies_list)


if st.button("Recommend"):
    re = recommend(select_movie_name)
    for i in re:
        st.write(i)
