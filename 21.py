#
# 21. Merge Two Sorted Lists
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.mergeTwoLists(
            l1=[1, 2, 4], l2=[1, 3, 4]), [1, 1, 2, 3, 4, 4])

    def test_2(self):
        self.assertEqual(self.s.mergeTwoLists(l1=[], l2=[]), [])

    def test_3(self):
        self.assertEqual(self.s.mergeTwoLists(l1=[], l2=[0]), [0])


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val >= l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


if __name__ == "__main__":
    unittest.main()
