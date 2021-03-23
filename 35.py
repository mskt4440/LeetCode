#
# 35. Search Insert Position
#
import unittest
import bisect


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.searchInsert(nums=[1, 3, 5, 6], target=5), 2)

    def test_2(self):
        self.assertEqual(self.s.searchInsert(nums=[1, 3, 5, 6], target=2), 1)

    def test_3(self):
        self.assertEqual(self.s.searchInsert(nums=[1, 3, 5, 6], target=7), 4)

    def test_4(self):
        self.assertEqual(self.s.searchInsert(nums=[1, 3, 5, 6], target=0), 0)

    def test_5(self):
        self.assertEqual(self.s.searchInsert(nums=[1], target=0), 0)


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)


if __name__ == "__main__":
    unittest.main()
