class Solution(object):
    def checkInclusion(self, s1, s2):
        f={}
        for ch in s1:
            if ch not in f:
                f[ch]=1
            else:
                temp=f[ch]
                f[ch]=temp+1
                
        left=0
        new={}
        for right in range(len(s2)):
            ch = s2[right]
            if ch not in new:
                new[ch]=1
            else:
                new[ch]+=1
            if(right-left+1)>len(s1):
                left+=1
                new[s2[left-1]]-=1
                if new[s2[left-1]]==0:
                    del new[s2[left-1]]
            if new == f:
                return True 
        return False 
