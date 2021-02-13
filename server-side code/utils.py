def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key
    return -1

def play(player1, player2):
    allowed = (0,1,2)
    if player1 not in allowed or player2 not in allowed:
        return (player1 - player2) % 3
    else:
        return -1