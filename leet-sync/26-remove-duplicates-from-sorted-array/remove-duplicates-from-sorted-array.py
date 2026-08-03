class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        tot = len(nums)

        while i < tot:
            j = i + 1
            count = 0
            while j < tot and nums[j] == nums[i]:
                count += 1
                j += 1

            for k in range(j, tot):
                nums[k - count] = nums[k]
            tot -= count

            i += 1

        return tot