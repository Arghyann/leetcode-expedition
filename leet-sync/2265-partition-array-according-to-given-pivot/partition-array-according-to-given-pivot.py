class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        greater=[]
        equal=[]
        for i in nums:
            if i<pivot:
                less.append(i)
            elif(i>pivot):
                greater.append(i)
            else:
                equal.append(i)
        result=less+equal+greater
        return result