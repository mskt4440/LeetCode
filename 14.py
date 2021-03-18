#
# 14. Longest Common Prefix
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")

    def test_2(self):
        self.assertEqual(self.s.longestCommonPrefix(
            ["dog", "racecar", "car"]), "")


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        if not strs:
            return ans
        for ws in zip(*strs):
            if len(set(ws)) != 1:
                break
            ans += ws[0]
        return ans


if __name__ == "__main__":
    unittest.main()
