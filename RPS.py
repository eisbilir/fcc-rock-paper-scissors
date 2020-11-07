# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

my_moves = ["R", "P", "S"]
ideal_response = {"P": "S", "R": "P", "S": "R"}


def player(prev_play, opponent_history=[]):
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)
    my_last_ten = my_moves[-10:]
    guess = ideal_response(min(set(my_last_ten), my_last_ten.count))
    return guess