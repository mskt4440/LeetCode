#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(numRows):
            if i == 0:
                ret.append([1])
                continue

            tmp = ret[-1][:]
            tmp.append(0)
            for i, p in enumerate(ret[-1]):
                tmp[i+1] += p
            ret.append(tmp)

        return ret
# @lc code=end
