class Solution(object):
    def gcdSum(self, nums):

        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        temp = []
        m=-1
        for i in range(len(nums)):
            if nums[i]>m:
                m=nums[i]
            num = nums[i]
            temp.append(gcd(m, num))
        temp.sort()
        sum = 0
        for i in range(len(temp) // 2):
            sum += gcd(temp[len(temp)-1-i],temp[i])
        return sum