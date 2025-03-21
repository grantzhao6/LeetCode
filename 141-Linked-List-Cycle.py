# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = set()
        curr = head
        while curr != None:
            if curr in d:
                return True
            d.add(curr)
            curr = curr.next
        return False

        