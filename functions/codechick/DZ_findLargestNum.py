# https://codechick.io/challenges/33


def findLargestNum(nums):
    if not nums:
        return []

    # big = float('-infinity')
    big = nums[0]
    for i in nums:
        if i > big:
            big = i
    return big
