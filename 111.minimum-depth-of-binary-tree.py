#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == right == 0:
            return 1
        elif left == 0 or right == 0:
            return (left or right)+1
        else:
            return min(left, right)+1

# @lc code=end
