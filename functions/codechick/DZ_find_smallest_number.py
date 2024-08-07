#https://codechick.io/challenges/32


def find_smallest_number(my_list):
    small = 1000000
    for i in my_list:
        if i < small:
            small = i
    return small