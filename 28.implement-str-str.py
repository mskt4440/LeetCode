#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh = len(haystack)
        ln = len(needle)
        ans = -1
        if ln == 0:
            ans = 0
        else:
            for i in range(lh-ln+1):
                if haystack[i:i+ln] == needle:
                    ans = i
                    break
        return ans

# @lc code=end
