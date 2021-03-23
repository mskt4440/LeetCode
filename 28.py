#
# 28 Implement strStr()
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.strStr(haystack="hello", needle="ll"), 2)

    def test_2(self):
        self.assertEqual(self.s.strStr(haystack="aaaaa", needle="bba"), -1)

    def test_3(self):
        self.assertEqual(self.s.strStr(haystack="a", needle="a"), 0)


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh = len(haystack)
        ln = len(needle)
        ans = -1
        if ln == 0:
            ans = 0
        else:
            for i in range(lh-ln+1):
                if haystack[i:i+ln] == needle:
                    ans = i
                    break
        return ans


if __name__ == "__main__":
    unittest.main()
