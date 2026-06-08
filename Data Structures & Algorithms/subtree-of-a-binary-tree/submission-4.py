# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(first, second):
            if not first and not second:
                return True
            if not first or not second:
                return False
            if first.val!=second.val:
                return False
            return same(first.left,second.left) and same(first.right,second.right)

        if not subRoot:
            return True
        if not root:
            return False
        q = deque([root])
        while q:
            node = q.pop()
            if node.val == subRoot.val and same(node, subRoot):
                return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


        return False