class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        nums3 = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        nums3.extend(nums1[i:])
        nums3.extend(nums2[j:])
        middle = len(nums3) // 2
        if len(nums3) % 2 == 1:
            print(nums3)
            return nums3[middle]
        else:
            print(nums3)
            return (nums3[middle] + nums3[middle - 1]) / 2.0

solution = Solution()
array1 = [17,22,35]
array2 = [78,85,98]
print("Median is:", solution.findMedianSortedArrays(array1, array2))
