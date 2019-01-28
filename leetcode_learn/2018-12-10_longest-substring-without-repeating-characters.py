# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 　这个提交失败
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         max_number = 0
#         number = 0
#         temp = ''
#         for i in s:
#             if i not in temp:
#                 temp += i
#                 number += 1
#             else:
#                 if number >= max_number:
#                     max_number = number
#
#                 index = temp.index(i)
#                 temp = temp[(index+1):] + i
#                 number = len(temp)
#
#             if number >= max_number:
#                 max_number = number
#
#             return max_number



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_max_len = 0
        temp_dict = {}
        max_len = 0
        start_index = 0

        for i in range(len(s)):
            if s[i] in temp_dict and temp_dict[s[i]] >= start_index:
                start_index = temp_dict[s[i]] + 1

            temp_max_len = i - start_index + 1
            temp_dict[s[i]] = i
            max_len = max(temp_max_len, max_len)

        return max_len
