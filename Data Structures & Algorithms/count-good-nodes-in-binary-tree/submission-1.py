# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # recursive
        # if not root:
        #     return 0
        # res = 0
        # # maintain a maximum num
        # def dfs(node, maximum):
        #     nonlocal res
        #     if not node:
        #         return
        #     if node.val >= maximum:
        #         res += 1
        #     maximum = max(node.val, maximum)
        #     dfs(node.left, maximum)
        #     dfs(node.right, maximum)
        # dfs(root, float('-inf'))
        # return res

        # iterative
        stack = [(root, root.val)]
        res = 0
        while stack:
            node, maximum = stack.pop()
            if not node:
                continue
            if node.val >= maximum:
                res += 1
            mval = max(maximum, node.val)
            if node.left:
                stack.append((node.left, mval))
            if node.right:
                stack.append((node.right, mval))
        return res
            




        



