# 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

# 超时
# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         str_dict = {}
#
#         if len(s) == 0:
#             return ''
#
#         max_len = 1
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 end_index = 0
#                 for k in range(len(s[i:j+1])):
#                     end_index = k
#                     if s[i:j+1][k] != s[i:j+1][-(k+1)]:
#                         break
#
#                 if end_index == len(s[i:j+1])-1:
#                     str_dict[len(s[i:j+1])] = s[i:j+1]
#
#                     if len(s[i:j+1]) >= max_len:
#                         max_len = len(s[i:j+1])
#
#         return str_dict[max_len]


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """






a = Solution()

s = "iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxzerakhmexuyeuhjfobrmkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfhevfesnwltekstsueefbrddxrmxokpaxsenwlgytdaexgfwtneurhxvjvpsliepgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrlspejqvzpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmaocesnpqaotamwofyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqxqobfsageysonuoagmmviozeouutsiecitrmkypwknorjjiaasxfhsftypspwhvqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacleqdxgrxbldcuxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexcybbjaxlfhyvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmucjlqpiolklmjxnscjcyiybdkgitxnuvtmoypcdldrvalxcxalpwumfx"
print(len(s))
res = a.longestPalindrome(s)
print(res)


