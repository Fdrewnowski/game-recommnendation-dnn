import streamlit as st
import pandas as pd
import argparse

from game_lib import load_data, calculate_point, get_top_n, get_games

parser = argparse.ArgumentParser(description='Run streamlit server')
parser.add_argument('--nonlp-rep-path', default='./names_and_reps-nonlp.pkl')
parser.add_argument('--nlp-rep-path', default='./names_and_reps-nlp.pkl')
parser.add_argument('--cbog-rep-path', default='./names_and_reps-cbog.pkl')
parser.add_argument('--fluff-data-path', default='./fluff_data.csv')
args = parser.parse_args()

@st.cache(suppress_st_warning=True)
def load_cached_data(model):
    if model == "NLP":
        return load_data(args.nlp_rep_path)
    if model == "CBoG":
        return load_data(args.cbog_rep_path)
    return load_data(args.nonlp_rep_path)

@st.cache(suppress_st_warning=True)
def get_fluff_df():
    return pd.read_csv('fluff_data.csv')

fluff = get_fluff_df()
st.header("Recomendation engine for games")
model = st.radio("Choose model for representations", ["No NLP", "NLP", "CBoG"])
data = load_cached_data(model)
unique_names = data['name'].unique()

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
    recomendations = pd.DataFrame(get_games(game_1, game_2, weight, data, number), columns=['Game name','Score'])
    st.header("TOP {} recomendations - the smaller score, the better!".format(number))
    recomendations_fluffed = recomendations.merge(fluff, how="left", left_on='Game name', right_on='name')[['Game name', 'Score', 'url', 'img_url']]
    for i, (index, rec) in enumerate(recomendations_fluffed.iterrows()):
    	col1, col2, col3 = st.columns([1, 6, 3])
    	col1.subheader(f"{i+1}")
    	col2.subheader(f"{rec['Game name']}, score: {rec['Score']:.3f}! [Store link!]({rec['url']})")
    	col3.image(f"{rec['img_url']}")
    	


