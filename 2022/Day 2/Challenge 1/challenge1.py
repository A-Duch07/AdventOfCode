# Day 2, challenge 1 of AOC2022 - counting score rock-paper-scissors
import numpy as np
import pandas as pd


# Score associated to each type of move : 1 for rock, 2 for paper and 3 for scissors
move_scores = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}

# Win-loss matrix for the player 
# To acces the player's score : wl_matrix.loc[player_move][opp_move]
wl_matrix = pd.DataFrame(np.array([[3, 0, 6], [6, 3, 0], [0, 6, 3]], np.uint8), index=['X', 'Y', 'Z'], columns=['A', 'B', 'C'])

# Init opponent and player scores
player_score = 0

# Parse the input and determine the score for the opponent and the player
with open('../input') as f:
    parsed_input = [tuple(line.rstrip('\n').split()) for line in f.readlines()]

    # For each round of rock-paper-scissor, calculate scores
    for round in parsed_input: 
        opp_move, player_move = round

        # Get initial scoring associated to shape selection then add the outcome of the round
        player_score += move_scores[player_move] + wl_matrix.loc[player_move][opp_move]

# Challenge 1 answer
print('Challenge 1 : ' + str(player_score))