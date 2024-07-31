# https://codechick.io/challenges/318


def XO(txt):
    x_char = 0
    o_char = 0
    for char in txt:
        char = char.upper()
        if char == "X":
            x_char = x_char + 1
        if char == "O":
            o_char = o_char + 1
    return x_char == o_char

