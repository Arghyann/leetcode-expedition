class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        sol=set()
        curr=[]
        for i in range(len(nums)-1):
            curr=[nums[i]]
            s=-nums[i]
            left=i+1
            right=len(nums)-1
            while right>left:
                insum=nums[right]+nums[left]
                if insum==s:
                    curr.append(nums[left])
                    curr.append(nums[right])
                    sol.add(tuple(curr))
                    curr=[nums[i]]
                    left += 1
                    right -= 1

                elif insum>s:
                    right-=1
                else:
                    left+=1
                
        return list(sol)