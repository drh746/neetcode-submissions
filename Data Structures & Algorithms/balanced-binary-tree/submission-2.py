# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
                
        # def dfs(node):
        #     if not node:
        #         return 0
        #     left = dfs(node.left)
        #     if left == -1:
        #         return -1
        #     right = dfs(node.right)
        #     if right == -1:
        #         return -1
        #     return 1 + max(left, right) if abs(left - right) <= 1 else -1
        # return dfs(root) != -1
        if not root:
            return True
        stack = [root]
        height = {}
        while stack:
            node = stack[-1]
            if node.left and node.left not in height:
                stack.append(node.left)
            elif node.right and node.right not in height:
                stack.append(node.right)
            else:
                left = height.get(node.left, 0)
                right = height.get(node.right, 0)
                if abs(left - right) > 1:
                    return False
                height[node] = 1 + max(left, right)
                stack.pop()
        return True

            





            
