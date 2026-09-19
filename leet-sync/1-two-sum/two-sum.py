class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i, val in enumerate(nums):
            if target - val in m:
                return [m[target - val], i]
            m[val] = i