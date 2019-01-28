# 给定
# n
# 个非负整数
# a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。在坐标内画
# n
# 条垂直线，垂直线
# i
# 的两个端点分别为(i, ai)
# 和(i, 0)。找出其中的两条线，使得它们与
# x
# 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且
# n
# 的值至少为
# 2。
#
#
#
# 图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为
# 49。
#
#
#
# 示例:
#
# 输入: [1, 8, 6, 2, 5, 4, 8, 3, 7]
# 输出: 49

# 最笨方法 超时
# class Solution:
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         max_area = 0
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 if i == j:
#                     continue
#
#                 if height[i] > height[j]:
#                     gao = height[j]
#                 else:
#                     gao = height[i]
#
#                 kuan = j - i
#                 area = gao * kuan
#                 if max_area < area:
#                     max_area = area
#
#         return max_area

# 指针法　一个头指针一个尾指针　将较矮的一边向较高的一边移动
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first_index = 0
        last_index = len(height)-1
        max_area = 0

        for i in range(len(height)):
            gao = min(height[first_index], height[last_index])
            # print('gao:'+str(gao))
            kuan = last_index - first_index
            # print('kuan'+ str(kuan))
            area = gao * kuan
            if area > max_area:
                max_area = area

            if height[first_index] >= height[last_index]:
                last_index -= 1
            else:
                first_index += 1

            if first_index >= last_index:
                break

        return  max_area






a = Solution()
height = [1,8,6,2,5,4,8,3,7]
res = a.maxArea(height)
print(res)
