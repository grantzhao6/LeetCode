# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        first = head
        second = head

        while n>0:
            if curr != None:
                curr = curr.next
            else:
                return head
            n-=1
        
        if curr == None:
            return head.next
        
        while curr != None:
            first = second
            second = second.next
            curr = curr.next
        
        first.next = second.next

        return head
        


        

        