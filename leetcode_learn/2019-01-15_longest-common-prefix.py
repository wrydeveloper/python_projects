# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。
# 最蠢方法
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        comment = ''
        sign = 0
        for i in range(len(strs[0])):
            temp = strs[0][:i+1]
            for j in range(len(strs)):
                if strs[j][:i+1] != temp:
                    sign = 0
                    break;
                else:
                    sign = 1

            if sign == 1:
                comment = temp

        return comment


a = Solution()
str = ['a', 'a']
res = a.longestCommonPrefix(str)
print(res)
