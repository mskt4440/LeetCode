#
# 1389. Create Target Array in the Given Order
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.createTargetArray(
            [0, 1, 2, 3, 4], [0, 1, 2, 2, 1]), [0, 4, 1, 3, 2])

    def test_2(self):
        self.assertEqual(self.s.createTargetArray(
            [1, 2, 3, 4, 0], [0, 1, 2, 3, 0]), [0, 1, 2, 3, 4])

    def test_3(self):
        self.assertEqual(self.s.createTargetArray([1], [0]), [1])


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        T = []  # type: List[int]
        for i, v in zip(index, nums):
            T.insert(i, v)

        return T


if __name__ == "__main__":
    unittest.main()
