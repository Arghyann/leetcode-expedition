class Solution():
    def search(self, nums, target):
        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return True
            if nums[left]==nums[mid] and nums[mid]==nums[right]:
                right-=1
                left+=1
                continue
            if nums[left]<=nums[mid] :
                if target < nums[mid] and target>=nums[left]:
                    right = mid -1 
                else:
                    left = mid + 1 
            if nums[right]>=nums[mid] :
                if target > nums[mid]  and target<=nums[right]:
                    left = mid +1
                else:
                    right = mid -1                 
        return False