# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive
        # def dfs(p, q):
        #     if not p and not q:
        #         return True
        #     elif not p or not q:
        #         return False
            
        #     return p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
        # return dfs(p, q)

        # Iterative
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()                
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            if n1.val == n2.val:
                stack.append((n1.left, n2.left))
                stack.append((n1.right, n2.right))
            else:
                return False
        return True


            
        