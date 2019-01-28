# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: 3
# 输出: "III"
# 示例 2:
#
# 输入: 4
# 输出: "IV"
# 示例 3:
#
# 输入: 9
# 输出: "IX"
# 示例 4:
#
# 输入: 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
# 示例 5:
#
# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >3999 or num < 0:
            return False

        if len(str(num)) == 4:
            res1 = self.gewei(int(str(num)[3]), 1)
            res2 = self.gewei(int(str(num)[2]), 2)
            res3 = self.gewei(int(str(num)[1]), 3)
            res4 = ''
            for i in range(int(str(num)[0])):
                res4 += 'M'

            res = res4 + res3 + res2 + res1
        elif len(str(num)) ==  3:
            res1 = self.gewei(int(str(num)[2]), 1)
            res2 = self.gewei(int(str(num)[1]), 2)
            res3 = self.gewei(int(str(num)[0]), 3)
            res = res3 + res2 + res1
        elif len(str(num)) ==  2:
            res1 = self.gewei(int(str(num)[1]), 1)
            res2 = self.gewei(int(str(num)[0]), 2)
            res = res2 + res1
        else:
            res = self.gewei(int(str(num)[0]), 1)

        return res

    def gewei(self, num, weishu):
        if weishu == 1:
            one = 'I'
            five = 'V'
            ten = 'X'
        elif weishu == 2:
            one = 'X'
            five = 'L'
            ten = 'C'
        elif weishu == 3:
            one = 'C'
            five = 'D'
            ten = 'M'

        if num <= 3:
            res = ''
            for i in range(num):
                res = res + one
        elif num == 4:
            res = one + five
        elif num == 9:
            res = one + ten
        else:
            res = five
            for i in range(num - 5):
                res = res + one

        return res

a = Solution()
res = a.intToRoman(1994)
print(res)

