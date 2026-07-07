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
        store = {}
        first = cur = head
        while first:
            store[first] = Node(first.val)
            first = first.next

        while cur:
            store[cur].next = store.get(cur.next)
            store[cur].random = store.get(cur.random)
            cur = cur.next
        return store.get(head)


