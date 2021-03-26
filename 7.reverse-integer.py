#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mx = 2**31-1
        s = 1
        X = ""
        if x >= 0:
            X = str(x)[::-1]
            n = len(X)
        else:
            mx += 1
            s = -1
            X = str(x)[1:][::-1]
        n = len(X)

        ans = 0
        r = mx
        for i, x in enumerate(X):
            t = int(x)*(10**(n-1-i))
            if t > r:
                ans = 0
                break
            ans += t
            r -= t

        return s*ans
# @lc code=end
