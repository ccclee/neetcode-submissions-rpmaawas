# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        currmax = root.val
        def localgoods(currmax, node):
            if not node:
                return 0
            if node.val >= currmax:
                currmax = node.val
                return localgoods(currmax, node.left) + localgoods(currmax, node.right) + 1
            else:
                return localgoods(currmax, node.left) + localgoods(currmax, node.right)

        return 1 + localgoods(currmax, root.left) + localgoods(currmax, root.right)

        