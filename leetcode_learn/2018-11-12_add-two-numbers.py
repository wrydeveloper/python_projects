# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        isaddone = 0 # 判断是否要加一
        temp = ListNode(0)
        res = temp
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next

            if l2:
                tmpsum += l2.val
                l2 = l2.next

            tempres = (tmpsum + isaddone) % 10
            isaddone = (tmpsum + isaddone) // 10
            res.next = ListNode(tempres)
            res = res.next

        if isaddone:
            res.next = ListNode(1)

        res = temp.next
        del temp
        return res


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = l11 =ListNode(4)
    l11.next = l12 = ListNode(5)

    l2 = ListNode(1)
    l2.next = l21 = ListNode(2)
    l21.next = l22 = ListNode(7)

    s = Solution()

    l3 = s.addTwoNumbers(l1, l2)
    print(l3.val)
    print(l3.next.val)
    print(l3.next.next.val)
