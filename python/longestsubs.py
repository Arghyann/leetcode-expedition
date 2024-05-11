class Solution(object):
    def lengthOfLongestSubstring(self, s):
        set1 = set()
        max_length = 0
        j = 0
        for i in range(len(s)):
            if s[i] in set1:
                while s[j] != s[i]:
                    set1.remove(s[j])
                    j += 1
                j += 1
            else:
                set1.add(s[i])
                max_length = max(max_length, len(set1))
        return max_length
solution=Solution()
input_string = "abcabcbb"
print(solution.lengthOfLongestSubstring(input_string))
