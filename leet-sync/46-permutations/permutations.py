class Solution(object):
    def permute(self, nums):
        
        if len(nums)==0:
            return [[]]
        ans=[]
        if(len(nums)!=0):
         removed=nums[0]
        copy=nums[:]
        copy.remove(copy[0])
        x=self.permute(copy)
        for z in x:
                for j in range(len(z)+1):
                    cp=z[:]
                    
                    cp.insert(j,removed)
                    ans.append(cp)
        return ans
             