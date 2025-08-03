class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return[[]]
        permutS=self.permute(nums[1:])
        result=[]
        for p in permutS:
            for i in range(len(p)+1):
                p_copy=p.copy()
                p_copy.insert(i,nums[0])
                result.append(p_copy)
        return result

