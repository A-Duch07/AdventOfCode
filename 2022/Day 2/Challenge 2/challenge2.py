# Day 2, challenge 2 of AOC2022 - counting score rock-paper-scissors with new rules
import numpy as np
import pandas as pd


# Score associated to each type of move : 1 for rock, 2 for paper and 3 for scissors
move_scores = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}

# Outcomes associated with values of input
outcomes = {
    'X' : 'Lose',
    'Y' : 'Draw',
    'Z' : 'Win',
}

# Win-loss matrix for the player 
# To acces the player's score : wl_matrix.loc[player_move][opp_move]
wl_matrix = pd.DataFrame(np.array([[3, 0, 6], [6, 3, 0], [0, 6, 3]], np.uint8), index=['X', 'Y', 'Z'], columns=['A', 'B', 'C'])

# Outcome matrix based on moves and their expected outcome
outcome_matrix = pd.DataFrame(np.array([['Y', 'X', 'Z'], ['Z', 'Y', 'X'], ['X', 'Z', 'Y']]), index=['A', 'B', 'C'], columns=['Win', 'Draw', 'Lose'])

# Init player scores
player_score = 0

# Parse the input and determine the score the player
with open('../input') as f:
    parsed_input = [tuple(line.rstrip('\n').split()) for line in f.readlines()]

    # For each round of rock-paper-scissor, calculate score based on outcome
    for round in parsed_input: 
        opp_move, outcome = round
        player_move = outcome_matrix.loc[opp_move][outcomes[outcome]]

        # Get initial scoring associated to shape selection then add the outcome of the round
        player_score += move_scores[player_move] + wl_matrix.loc[player_move][opp_move]

# Challenge 2 answer
print('Challenge 2 : ' + str(player_score))