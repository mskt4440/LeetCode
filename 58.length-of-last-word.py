#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = list(s.split())
        if not L:
            return 0
        else:
            return len(L[-1])
# @lc code=end
