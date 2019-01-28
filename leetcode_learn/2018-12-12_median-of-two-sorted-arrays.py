# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import math
        nums = nums1 + nums2
        if len(nums1) != 0 and len(nums2) != 0:
            nums.sort()
            if len(nums) > 2:
                if len(nums) % 2 == 0:
                    res = (nums[math.floor(len(nums) / 2)] + nums[math.floor(len(nums) / 2) - 1]) / 2
                else:
                    res = nums[math.floor(len(nums) / 2)]
            else:
                res = (nums[0] + nums[1]) / 2
        else:
            if len(nums1) == 0 and len(nums2) > 2:
                nums2.sort()
                if len(nums2) % 2 == 0:
                    res = (nums2[math.floor(len(nums2) / 2)] + nums2[math.floor(len(nums2) / 2) - 1]) / 2
                else:
                    res = nums2[math.floor(len(nums2) / 2)]
            elif len(nums2) == 0 and len(nums1) > 2:
                nums1.sort()
                if len(nums1) % 2 == 0:
                    res = (nums1[math.floor(len(nums1) / 2)] + nums1[math.floor(len(nums1) / 2) - 1]) / 2
                else:
                    res = nums1[math.floor(len(nums1) / 2)]
            elif len(nums1) == 0 and len(nums2) == 1:
                res = nums2[0]
            elif len(nums2) == 0 and len(nums1) == 1:
                res = nums1[0]
            elif len(nums1) == 0 and len(nums2) == 2:
                res = (nums2[0] + nums2[1]) / 2
            elif len(nums2) == 0 and len(nums1) == 2:
                res = (nums1[0] + nums1[1]) / 2

        return res


n = Solution()

num1 = [1, 2, 3, 4, 5]
num2 = []

print(n.findMedianSortedArrays(num1, num2))


