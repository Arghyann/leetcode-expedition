class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        if target>nums[right]:
            return right+1

        while right>left:
            mid=left+(right-left)//2
            if(target>nums[mid]):
                left=mid+1
            elif target == nums[mid]:
                return mid 
            else:
                right = mid 
        
        return right 
