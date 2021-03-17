#
# 9. Palindrome Number
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.isPalindrome(121), True)

    def test_2(self):
        self.assertEqual(self.s.isPalindrome(-121), False)

    def test_3(self):
        self.assertEqual(self.s.isPalindrome(10), False)

    def test_4(self):
        self.assertEqual(self.s.isPalindrome(-101), False)


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[::-1] == str(x):
            return True
        else:
            return False


if __name__ == "__main__":
    unittest.main()
