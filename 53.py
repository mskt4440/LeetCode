#
# 53. Maximum Subarray
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.maxSubArray(
            nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_2(self):
        self.assertEqual(self.s.maxSubArray(nums=[1]), 1)

    def test_3(self):
        self.assertEqual(self.s.maxSubArray(nums=[5, 4, -1, 7, 8]), 23)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        dp.append(nums[0])
        ans = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            ans = max(ans, dp[i])
        return ans


if __name__ == "__main__":
    unittest.main()
