#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[n-1]:
                n += 1
                nums[n-1] = nums[i]
        return n
# @lc code=end
