"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # interweavie nodes A->B->C A->A'->B->B'->C->C'
        cur = head
        while cur:
            node = Node(cur.val)
            temp = cur.next
            cur.next = node
            node.next = temp
            cur = temp
        # A'.random = A.random.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # unchain A->A'->B->B'->C->C'
        dummy = Node(0)
        res = dummy
        cur = head
        while cur:
            res.next = cur.next
            res = res.next
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next




