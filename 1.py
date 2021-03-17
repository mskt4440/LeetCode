#
# 1. Two Sum
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(self.s.twoSum([3, 2, 4, 6], 6), [1, 2])

    def test_3(self):
        self.assertEqual(self.s.twoSum([3, 3], 6), [0, 1])


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v1 in enumerate(nums[:-1]):
            for j, v2 in enumerate(nums[i+1:], i+1):
                if v1+v2 == target:
                    return([i, j])


if __name__ == "__main__":
    unittest.main()
