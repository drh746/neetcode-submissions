# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        store = set()
        cur = head
        while cur:
            if cur in store:
                return True
            store.add(cur)
            cur = cur.next
        return False