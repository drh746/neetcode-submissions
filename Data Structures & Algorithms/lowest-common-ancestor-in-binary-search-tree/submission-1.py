# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        while root:
            low, high = min(p.val, q.val), max(p.val, q.val)
            if low > root.val:
                root = root.right
            elif high < root.val:
                root = root.left
            else:
                return root


