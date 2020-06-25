# Given an array S of n integers, find three
# integers in S such that the sum is closest
# to a given number, target. Return the
# difference  between the sum of the
# three integers and the given number.
# You may assume that each input would have exactly one solution.

# Example
# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to
# the target is 2. (-1 + 2 + 1 = 2)
# and the difference is 1.

import sys


class Solution(object):
    def threeSumClosest(self, num, target):
        """
    input: int[] num, int target
    return: int
    """
        # write your solution here
        minDiff = sys.maxsize
        num.sort()
        for i in range(len(num)):
            firstV = num[i]
            numLeft = num[i + 1 :]
            newTarget = target - firstV
            diff = self.twoSumClosest(numLeft, newTarget)
            if minDiff > diff:
                minDiff = diff
            if minDiff == 0:
                return 0
        return minDiff

    def twoSumClosest(self, nums, target):
        # nums -> min - max
        pMin = 0
        pMax = len(nums) - 1
        minDiff = sys.maxsize

        # optimize
        if len(nums) <= 1:
            return minDiff

        while minDiff != 0 and pMin < pMax:
            sums = nums[pMin] + nums[pMax]
            diff = abs(sums - target)
            if minDiff > diff:
                minDiff = diff
            if sums > target:
                pMax -= 1
            else:
                pMin += 1
        return minDiff
