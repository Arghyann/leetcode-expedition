class Solution(object):
    def findMin(self, nums):
        left=0
        right=len(nums)-1
        while right > left: 
            mid = left + (right - left)//2
            print(mid)
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]>nums[right]:
                left = mid + 1 
            else:
                right=mid
        return nums[right]

        