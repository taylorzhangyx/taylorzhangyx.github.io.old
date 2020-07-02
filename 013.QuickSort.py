import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick(nums, l, r):
            if r - l < 1:
                return

            p = random.randint(l, r)
            nums[p], nums[r] = (
                nums[r],
                nums[p],
            )  # need to move the selected v to the end of the list
            less = l
            for i in range(l, r):
                cur = nums[i]
                if cur <= nums[r]:
                    nums[less], nums[i] = nums[i], nums[less]
                    less += 1
            nums[r], nums[less] = nums[less], nums[r]
            # print(nums,l,r,p,less)
            quick(nums, l, less - 1)
            quick(nums, less + 1, r)

        quick(nums, 0, len(nums) - 1)
        return nums
