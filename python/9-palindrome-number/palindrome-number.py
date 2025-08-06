class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        if(y==y[::-1]):
            return True
        return False