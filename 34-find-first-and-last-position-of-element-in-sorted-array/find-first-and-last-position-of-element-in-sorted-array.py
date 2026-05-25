class Solution(object):
    def searchRange(self, nums, target):
        if (len(nums)==0):
            return -1,-1
        left=0
        right=len(nums)-1
        first=-1
        last=-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                last=mid
                left=mid+1
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                first=mid
                right=mid-1
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return first,last