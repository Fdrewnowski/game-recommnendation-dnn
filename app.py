import streamlit as st
import pandas as pd

from game_lib import load_data, calculate_point, get_top_n, get_games


data = load_data("./names_and_reps.pkl")

unique_names = data['name'].unique()

st.header("Recomendation engine for games")

game_1 = st.selectbox(
     'Game one',
     unique_names)

st.write('You selected game 1:', game_1)

game_2 = st.selectbox(
     'Game two:', unique_names.copy())

st.write('You selected game 2:', game_2)

weight = st.slider('Select weight for first game:', 0.0, 1.0, 0.5)
st.write("First game weight:", weight)

number = st.number_input('Select number of recomendations:', 0,50,10)
st.write('Show top',number,' recomendations')

if game_1 and game_2 and weight and number and st.button('Search'):
    recomendations = get_games(game_1, game_2, weight, data, number)
    st.write("TOP{} recomendations score smaller the better".format(number))
    st.write(pd.DataFrame(recomendations, columns=['Game name','Score']))


