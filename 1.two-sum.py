#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v1 in enumerate(nums[:-1]):
            for j, v2 in enumerate(nums[i+1:], i+1):
                if v1+v2 == target:
                    return([i, j])
# @lc code=end
