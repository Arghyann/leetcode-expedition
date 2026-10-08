class Solution(object):
    def removeOuterParentheses(self, s):
       stack = []
       newS="" 
       curr=""
       for i in range(len(s)):
        if s[i]=='(':
            stack.append(1)
            curr=curr+s[i]
        else:
            stack.pop()
            curr= curr+s[i]
        if i!=0 and len(stack)==0:
            newS=newS+curr[1:-1] 
            curr=""
       return newS