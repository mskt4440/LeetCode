#
# 13. Roman to Integer
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.romanToInt("III"), 3)

    def test_2(self):
        self.assertEqual(self.s.romanToInt("IV"), 4)

    def test_3(self):
        self.assertEqual(self.s.romanToInt("IX"), 9)

    def test_4(self):
        self.assertEqual(self.s.romanToInt("LVIII"), 58)

    def test_5(self):
        self.assertEqual(self.s.romanToInt("MCMXCIV"), 1994)


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("CM", "m").replace("CD", "d")
        s = s.replace("XC", "c").replace("XL", "l")
        s = s.replace("IX", "x").replace("IV", "v")

        ans = 0
        for w in s:
            if w == "M":
                ans += 1000
            elif w == "m":
                ans += 900
            elif w == "D":
                ans += 500
            elif w == "d":
                ans += 400
            elif w == "C":
                ans += 100
            elif w == "c":
                ans += 90
            elif w == "L":
                ans += 50
            elif w == "l":
                ans += 40
            elif w == "X":
                ans += 10
            elif w == "x":
                ans += 9
            elif w == "V":
                ans += 5
            elif w == "v":
                ans += 4
            else:
                ans += 1

        return ans


if __name__ == "__main__":
    unittest.main()
