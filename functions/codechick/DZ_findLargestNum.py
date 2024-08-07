#https://codechick.io/challenges/33


def findLargestNum(nums):
    big = 0
    for i in nums:
        if i > big:
            big = i
    return big      