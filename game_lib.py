from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler
import pandas as pd

def load_data(file_name):
    names_and_reps = pd.read_pickle(file_name)
    return names_and_reps


def calculate_point(first_game, second_game, weight):
    result = [0]*len(first_game)

    for index in range(len(first_game)):
        difference_tmp = abs(first_game[index] - second_game[index])
        if first_game[index] > second_game[index]:
            result[index] = first_game[index] - (difference_tmp * (1-weight))
        elif first_game[index] < second_game[index]:
            result[index] = first_game[index] + (difference_tmp * (1-weight))
        else:
            result[index] = 0
    return result


def get_top_n(target,data, n, standarize=True):
    vals = data['representation'].values.tolist()
    target = [target]
    if standarize:
        ss = StandardScaler()
        vals = ss.fit_transform(vals)
        target = ss.transform(target)
    all_dist = euclidean_distances(vals,target)
    indexes = all_dist.flatten().argsort()[:n]
    games = []
    for ind in list(indexes):
        games.append((data['name'].iloc[ind], all_dist.flatten()[ind]))
    return games


def get_games(first_name, second_name, weight, data, n):
    try:
        first_game = data[data['name']==first_name]['representation'].values[0]
        second_game = data[data['name']==second_name]['representation'].values[0]
    except:
        print("No such games in dataset")
        return [()]
    game_in_space = calculate_point(first_game, second_game, weight)
    games = get_top_n(game_in_space, data, n)
    return games