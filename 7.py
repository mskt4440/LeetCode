#
# 7. Reverse Integer
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.reverse(123), 321)

    def test_2(self):
        self.assertEqual(self.s.reverse(-123), -321)

    def test_3(self):
        self.assertEqual(self.s.reverse(120), 21)

    def test_4(self):
        self.assertEqual(self.s.reverse(0), 0)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mx = 2**31-1
        s = 1
        X = ""
        if x >= 0:
            X = str(x)[::-1]
            n = len(X)
        else:
            mx += 1
            s = -1
            X = str(x)[1:][::-1]
        n = len(X)

        ans = 0
        r = mx
        for i, x in enumerate(X):
            t = int(x)*(10**(n-1-i))
            if t > r:
                ans = 0
                break
            ans += t
            r -= t

        return s*ans


if __name__ == "__main__":
    unittest.main()
