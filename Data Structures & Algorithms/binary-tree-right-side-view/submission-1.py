# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS:
        # if not root:
        #     return []
        # q = deque([root])
        # res = []
        # while q:
        #     n = len(q)
        #     for i in range(n):
        #         node = q.popleft()
        #         if i == n - 1:
        #             res.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return res

        # dfs
        if not root:
            return []
        res = []
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res

            


