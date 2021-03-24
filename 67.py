#
# 67. Add Binary
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.addBinary(a="11", b="1"), "100")

    def test_2(self):
        self.assertEqual(self.s.addBinary(a="1010", b="1011"), "10101")


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    unittest.main()
