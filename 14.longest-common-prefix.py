#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
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
# @lc code=end
