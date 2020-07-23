# 给定一个含有 n 个正整数的数组和一个正整数 s ，
# 找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
# 并返回其长度。
# 如果不存在符合条件的连续子数组，返回 0。
# 示例: 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 输入: s = 3, nums = [1, 1]
# 输出: 0
# 解释: 不存在长度最小的连续子数组


def updateres(sumN, currentsmall, left, right, s):

    if sumN >= s:
        if currentsmall == -1:
            return right - left
        else:
            return min(right - left, currentsmall)
    return currentsmall


def smallest(nums, s):
    smallestlength = -1
    left, right = 0, 0
    sumN = 0
    for i in range(len(nums)):
        sumN += nums[right]
        right += 1
        smallestlength = updateres(sumN, smallestlength, left, right, s)
        # move left till sum is smaller than s
        while sumN >= s:
            sumN -= nums[left]
            left += 1
            smallestlength = updateres(sumN, smallestlength, left, right, s)
    if smallestlength == -1:
        return 0
    else:
        return smallestlength


print(smallest([2, 3, 1, 2, 4, 3], 7))
print(smallest([1, 1], 3))
