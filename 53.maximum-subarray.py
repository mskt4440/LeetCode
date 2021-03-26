#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
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

# @lc code=end
