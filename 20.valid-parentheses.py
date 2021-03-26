#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ("(", "[", "{")
        right = (")", "]", "}")
        stack = collections.deque()

        ans = True
        for w in s:
            if w in right:
                if not stack or left[right.index(w)] != stack[-1]:
                    ans = False
                    break
                else:
                    stack.pop()
            if w in left:
                stack.append(w)
        if stack:
            ans = False
        return ans
# @lc code=end
