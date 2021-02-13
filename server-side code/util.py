def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"