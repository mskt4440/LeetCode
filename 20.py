#
# 20. Valid Parentheses
#
import unittest
import collections


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.isValid("()"), True)

    def test_2(self):
        self.assertEqual(self.s.isValid("()[]{}"), True)

    def test_3(self):
        self.assertEqual(self.s.isValid("(]"), False)

    def test_4(self):
        self.assertEqual(self.s.isValid("([(]"), False)

    def test_5(self):
        self.assertEqual(self.s.isValid("{[]}"), True)


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ("(", "[", "{")
        right = (")", "]", "}")
        stack = collections.deque()

        ans = True
        for w in s:
            if w in right:
                if not stack or left[right.index(w)] != stack[-1]:
                    ans = False
                    break
                else:
                    stack.pop()
            if w in left:
                stack.append(w)
        if stack:
            ans = False
        return ans


if __name__ == "__main__":
    unittest.main()
