# Day 4, challenge 1 of AoC2024 - 
import re
import pandas as pd

# Simple matching function for XMAS for concision sake
def number_of_matches(input: str) -> int:
    return len(re.findall(r'XMAS|xmas', input))

# Loop through a diagonals values based on the current row and column, 
# as well as the total number of rows and columns
def iter_diag(df: pd.DataFrame, row_index: int, col_index: int, nb_row: int, nb_col: int) -> str:
    current_diag: str = '' # current diagonal storage
    while row_index != nb_row and col_index != nb_col:
        current_diag += df[col_index][row_index]
        row_index += 1
        col_index += 1
    
    return current_diag # Adding whitespace to seperate the diagonals in the string (so as not to create involuntary XMAS combinations between diagonals)

# Function to extract all the diagonals into one string for matching of XMAS
def diagonal_str_extraction(df: pd.DataFrame) -> str:
    extracted_diagonal: str = '' # Extracted diagonal string
    nb_row, nb_col = df.shape

    # Iterate over each column of the puzzle's dataframe (our provided input)
    for col_index, col_chars in df.items():
        # When doing the first column, we tackle all the diagonals below it as well. Doing so means we don't
        # have to do anything but the higher diagonals after the first column.
        if col_index == 0:
            for row_index, _ in col_chars.items():
                extracted_diagonal += iter_diag(df, row_index, col_index, nb_row, nb_col)
        else:
            extracted_diagonal += iter_diag(df, 0, col_index, nb_row, nb_col)
    
    return extracted_diagonal
   

with open('../input') as f:
    # Extract the puzzle from the file to a list of strings and to a df, for easier manipulations on complexe operations
    word_search_puzzle:list[str] = [line.strip('\n') for line in f.readlines()]
    word_search_df: pd.DataFrame = pd.DataFrame(data=[list(line) for line in word_search_puzzle])

    # Get the word search puzzle
    horizontal_search:str = ''.join(word_search_puzzle)
    reversed_horizontal_search:str = horizontal_search[::-1] # Reverse the word search puzzle to check for backwards XMAS patterns

    # Create a vertical string of the word search. Apparently, its faster to iterate through cols than rows in pandas, so that's what I did. No need to transpose matrix
    vertical_search:str = ''.join([''.join(col.to_numpy().tolist()) for _, col in word_search_df.items()])
    reversed_vertical_search: str = vertical_search[::-1] # Reverse the word search puzzle to check for backwards XMAS patterns

    # Create a diagonal (left to right) string of the word search
    diagonal_lr_search: str = diagonal_str_extraction(word_search_df)
    reversed_diagonal_lr_search: str = diagonal_lr_search[::-1]

    # Create a diagonal (right to left) string of the word search\
    mirrored_word_search: list = []
    for _, col in word_search_df.items():
        mirrored_word_search.insert(0, col)
    diagonal_rl_search: str = diagonal_str_extraction(pd.DataFrame(mirrored_word_search).transpose())
    reversed_diagonal_rl_search: str = diagonal_rl_search[::-1]

    total_found = number_of_matches(horizontal_search) + number_of_matches(reversed_horizontal_search) +\
        number_of_matches(vertical_search) + number_of_matches(reversed_vertical_search) +\
        number_of_matches(diagonal_lr_search) + number_of_matches(reversed_diagonal_lr_search) +\
        number_of_matches(diagonal_rl_search) + number_of_matches(reversed_diagonal_rl_search)
    
    print(total_found)