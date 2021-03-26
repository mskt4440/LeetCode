#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = []
        t = 1
        for d in digits[::-1]:
            if d + t == 10:
                ret.append(0)
            else:
                ret.append(d+t)
                t = 0
        if t == 1:
            ret.append(t)
        return list(reversed(ret))
# @lc code=end
