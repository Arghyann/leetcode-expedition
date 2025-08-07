class Solution(object):
    def reverse(self, x):
        isneg=False
        num=x
        if x<0:
            isneg=True
            num=x-(2*x)
        num=str(num)
        num=num[::-1]
        num=int(num)
        if -(2**31) <= num <= 2**31 - 1:
            if isneg:
                return -num
            return num
        return 0