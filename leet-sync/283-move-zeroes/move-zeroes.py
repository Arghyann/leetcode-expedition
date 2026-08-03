class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[write]=nums[i]
                write+=1
        for i in range(write,len(nums)):
            nums[i]=0
            
        return nums