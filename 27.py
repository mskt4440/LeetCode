#
# 27. Remove Element
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.removeElement(nums=[3, 2, 2, 3], val=3), 2)

    def test_2(self):
        self.assertEqual(self.s.removeElement(
            nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2), 5)


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[n] = nums[i]
                n += 1
        return n


if __name__ == "__main__":
    unittest.main()
