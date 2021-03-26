#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x+1
        while abs(r-l) > 1:
            mid = (l+r)//2
            if mid**2 <= x:
                l = mid
            else:
                r = mid
        return l
# @lc code=end
