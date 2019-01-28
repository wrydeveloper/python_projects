# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

##################################################################
#
#   两数之和
#
##########################################################
class Solution:
    def twoSum(self, nums, target=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if nums[i] in temp:
                return temp[nums[i]], i
            else:
                temp[res] = i

        # 超时
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return i, j
        #
        # # 超时
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i < j:
        #             if target - nums[i] == nums[j]:
        #                 return i, j
        #
        # # 通过 1364ms
        # for i in range(len(nums)):
        #     res = target - nums[i]
        #     if res in nums and i != nums.index(res):
        #         return i, nums.index(res)

        # 通过 48ms
        # arr = {}
        # for i in range(len(nums)):
        #     res = target - nums[i]
        #     if nums[i] not in arr: # 检查当前值是不是以及存在字典中
        #         arr[res] = i # 把差值作为key, 索引作为val 存入字典
        #     else:
        #         return arr[nums[i]], i

        # 通过 44ms  利用dict中　ｋｅｙ是唯一来做
        arr = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if nums[i] in arr:
                return arr[nums[i]], i
            else:
                arr[res] = i

a = Solution()

b = a.twoSum([2, 7, 11, 15], 9)

print(b)
