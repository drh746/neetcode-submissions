# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Recursive
        # def identical(n1, n2):
        #     if not n1 and not n2:
        #         return True
        #     if not n1 or not n2:
        #         return False
        #     return n1.val == n2.val and identical(n1.left, n2.left) and identical(n1.right, n2.right)
        # if not subRoot:
        #     return True
        # if not root:
        #     return False
        # if identical(root, subRoot):
        #     return True
        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # Iterative
        def identical(node, subRoot):
            s = [(node, subRoot)]
            while s:
                p, q = s.pop()
                if not p and not q:
                    continue
                elif not p or not q:
                    return False
                if p.val == q.val:
                    s.append((p.left, q.left))
                    s.append((p.right, q.right))
                else:
                    return False
            return True

        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if identical(node, subRoot):
                return True
            stack.append(node.left)
            stack.append(node.right)
        return False

        


        