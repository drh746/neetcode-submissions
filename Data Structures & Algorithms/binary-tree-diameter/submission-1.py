# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive
        # self.res = 0
        # def dfs(node):
        #     if not node:
        #         return 0
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     self.res = max(left + right, self.res)
        #     return 1 + max(left, right)
        # dfs(root)
        # return self.res

        # Iterative
        if not root:
            return 0
        stack = [root]
        height = {}
        self.res = 0
        while stack:
            node = stack[-1]
            if node.left and node.left not in height:
                stack.append(node.left)
            elif node.right and node.right not in height:
                stack.append(node.right)
            else:
                left = height.get(node.left, 0)
                right = height.get(node.right, 0)
                self.res = max(self.res, left + right)
                height[node] = 1 + max(left, right)
                stack.pop()
        return self.res




        





        

