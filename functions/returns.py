# return - возврат
# ----------------------------
# def say_hello(name):
#     print(f'Привет, {name}!')
#
#     # return None
#     return -1
#     print('Я здесь')


# result = say_hello('Андрей')
# print(result)

# -------------------------------------

# def get_hello(name):
#     return f'Привет, {name}!'
#     # print(f'Привет, {name}!')
#
#     # return None
#
# data = get_hello('Андрей')
# print(data)


# -------------------------------------

# def add(a, b):
#     return a + b
#
#
# first = 5
# second = 2
#
# res = add(first, second)
#
# print(res * 2)


# CTRL + . (точка)


# -------------------------------------

# def add_or_multiple(a, b):
#     # if a > 10 and b > 10:
#     #     return a + b
#     # else:
#     #     return a * b
#
#     if a > 10 and b > 10:
#         return a + b
#     return a * b
#
#
# res = add_or_multiple(3, 5)
# print(res)

# -------------------------------------

numbers = [1, 2, 3, 4, 5]


def custom_sum(nums):
    total = 0
    for n in nums:
        # total = total + n
        total += n

    return total


res = sum(numbers)
print(res)

res_2 = custom_sum(numbers)
print(res_2)
