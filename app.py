import streamlit as st
import pickle
import pandas as pd
import requests

#bfbcfa5a02f05b3ca60dd3098476380c
#to fetch posteofrs  movie
@st.cache_resource
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bfbcfa5a02f05b3ca60dd3098476380c&language=en-US"
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"


#main function, new_df=movies and similarity matrix is imported
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters=[]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch posters from api
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movie_posters

#import df and sim.matrix
#movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
#similarity = pickle.load(open('similarity.pkl', 'rb'))
#dataframe
@st.cache_resource
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies_dict, similarity

movies_dict, similarity = load_data()

movies = pd.DataFrame(movies_dict)

#searchbar
st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
'What Movie do you want to recommend?',
    movies['title'].values
)

#button
#if st.button('Recommend'):
 #   recommendations = recommend(selected_movie_name)
  #  for i in recommendations:
   #     st.write(i)
if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        #for movie_name in recommended_movie_names:
         # st.text(movie_name)
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        #if len(recommended_movie_posters) > 4:
         #   st.image(recommended_movie_posters[4])
