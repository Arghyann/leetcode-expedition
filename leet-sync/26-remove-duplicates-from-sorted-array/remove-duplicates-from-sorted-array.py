class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write=0
        replaced=float('inf')
        for i in range(len(nums)):
            if nums[i]!=replaced:
                nums[write]=nums[i]
                write+=1
                replaced=nums[i]
        return write