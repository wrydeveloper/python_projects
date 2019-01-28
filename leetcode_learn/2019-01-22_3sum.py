# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 超时
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         arrs = []
#
#         # nums = list(set(nums))
#
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         arr = [nums[i], nums[j], nums[k]]
#                         if sorted(arr) in arrs:
#                             continue
#                         else:
#                             arrs.append(sorted(arr))
#
#         return arrs

# 太慢了
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums = sorted(nums)
#         arr = []
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             first_index = i + 1
#             last_index = len(nums) - 1
#             now_num = 0 - nums[i]
#             # if nums[first_index] == nums[first_index-1]:
#             #     continue
#
#             while first_index < last_index:
#                 if nums[first_index] + nums[last_index] == now_num:
#                     if [nums[i], nums[first_index], nums[last_index]] not in arr:
#                         arr.append([nums[i], nums[first_index], nums[last_index]])
#
#                     while first_index < last_index and nums[first_index] == nums[first_index+1]:
#                         first_index += 1
#
#                     while first_index < last_index and nums[last_index] == nums[last_index-1]:
#                         last_index -= 1
#
#                     first_index +=1
#                     last_index -= 1
#                 elif nums[first_index] + nums[last_index] < now_num:
#                     first_index += 1
#                 else:
#                     last_index -= 1
#
#         return arr

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()  # 排序
        res = []

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:  # 避免相同值
                            print(l)
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            print(r)
                            r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return res


a = Solution()
nums = [-1, -1,0,0,1,2,-1,-4, -4]
res = a.threeSum(nums)
print(res)
