class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        ans=[0]*(len(nums))
        ansi=len(nums)-1
        while right>=left:
            sqrl=nums[left]**2
            sqrr=nums[right]**2
            if sqrl>sqrr:
                ans[ansi]=sqrl
                left+=1
            else:
                print(ansi)
                ans[ansi]=sqrr
                right-=1
            ansi-=1
        return ans