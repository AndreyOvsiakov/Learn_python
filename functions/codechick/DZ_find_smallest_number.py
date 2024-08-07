# https://codechick.io/challenges/32


def find_smallest_number(my_list):
    if not my_list:
        return []

    # small = float('infinity')
    small = my_list[0]
    for i in my_list:
        if i < small:
            small = i
    return small
