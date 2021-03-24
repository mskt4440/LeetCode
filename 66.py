#
# 66. Plus One
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.plusOne(digits=[1, 2, 3]), [1, 2, 4])

    def test_2(self):
        self.assertEqual(self.s.plusOne(digits=[4, 3, 2, 1]), [4, 3, 2, 2])

    def test_3(self):
        self.assertEqual(self.s.plusOne(digits=[0]), [1])


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = []
        t = 1
        for d in digits[::-1]:
            if d + t == 10:
                ret.append(0)
            else:
                ret.append(d+t)
                t = 0
        if t == 1:
            ret.append(t)
        return list(reversed(ret))


if __name__ == "__main__":
    unittest.main()
