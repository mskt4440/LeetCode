#
# 58. Length of Last Word
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.lengthOfLastWord(s="Hello World"), 5)

    def test_2(self):
        self.assertEqual(self.s.lengthOfLastWord(s=" "), 0)


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = list(s.split())
        if not L:
            return 0
        else:
            return len(L[-1])


if __name__ == "__main__":
    unittest.main()
