# MAX WATER TRAPPED
# Given a non-negative integer array representing the heights of a list of adjacent bars. Suppose each bar has a width of 1. Find the largest amount of water that can be trapped in the histogram.

# Assumptions
# The given array is not null
# Examples
# { 2, 1, 3, 2, 4 }, the amount of water can be trapped is 1 + 1 = 2 (at index 1, 1 unit of water can be trapped and index 3, 1 unit of water can be trapped)


class Solution(object):
    def maxTrapped(self, array):
        """
    input: int[] array
    return: int
    """
        # write your solution here
        # start checking
        if len(array) <= 2:
            return 0

        # init
        water = 0
        left = 0
        que = list()

        def calculateWater(h):
            waterT = 0
            right = h
            while len(que) != 0:
                curH = array[que.pop()]
                diff = min(left, right) - curH
                waterT += diff if diff > 0 else 0
                right = max(h, curH)
            return waterT

        for i in range(len(array)):
            curr = array[i]
            if curr < left:
                que.append(i)
            else:
                water += calculateWater(curr)
                left = curr

        water += calculateWater(0)
        return water
