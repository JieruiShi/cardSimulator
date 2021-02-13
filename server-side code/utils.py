def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key
    return -1



def play(player1, player2):
    result = player1 - player2
    if result % 3 == 0:
        return 0
    elif result % 3 == 1:
        return 1
    elif result % 3 == 2:
        return 2
    else:
        return -1