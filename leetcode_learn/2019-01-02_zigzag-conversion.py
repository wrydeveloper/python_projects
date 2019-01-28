# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
#
#L       I
#E     E S     G
#E   D   H   N
#T O     I I
#C       R

class Solution:
    def convert(self, s, numRows):
        """3 1 4 2 5 3
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s

        a = {}
        for i in range(numRows):
            a[i] = ''

        for i in range(len(s)):
            yushu = i % (numRows+numRows-2)
            beishu = int(i / (numRows+numRows-2))

            if yushu <= (numRows-1):
                x = beishu*(1+numRows-2)
                y = yushu
            elif yushu > (numRows-1) and yushu <= (numRows+numRows-2-1):
                weizhi = yushu - (numRows - 1)
                y = numRows - 1 - weizhi
                x = beishu*(1+numRows-2) + weizhi

            a[y] = str(a[y]) + str(s[i])

        res = ''
        for i in range(numRows):
            res += a[i]

        return res

s = "LEETCODEISHIRING"
a = Solution()
b = a.convert(s, 4)
print(b)