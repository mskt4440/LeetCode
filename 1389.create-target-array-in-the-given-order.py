#
# @lc app=leetcode id=1389 lang=python
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        T = []  # type: List[int]
        for i, v in zip(index, nums):
            T.insert(i, v)

        return T
# @lc code=end
