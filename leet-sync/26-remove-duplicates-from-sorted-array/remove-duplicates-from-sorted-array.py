class Solution(object):
    def removeDuplicates(self, nums):
        write=0
        curr=float('-inf')
        for i in range(len(nums)):
            if(curr!=nums[i]):
                nums[write]=nums[i]
                curr=nums[i]
                write+=1
        return write