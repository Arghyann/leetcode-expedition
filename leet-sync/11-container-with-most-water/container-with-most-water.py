class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height)-1
        ans = 0
        while left < right:
            area = (right - left )*min(height[left],height[right])
            if area > ans :
                ans = area
            print(area)
            print(ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return ans