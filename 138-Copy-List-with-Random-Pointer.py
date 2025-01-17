\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        d = {}

        curr = head
        while curr != None:
            d[curr] = Node(curr.val,None,None)
            curr = curr.next
        
        curr = head
        while curr != None:
            if curr.next != None:
                d[curr].next =  d[curr.next]
            if curr.random != None:
                d[curr].random = d[curr.random]
            curr = curr.next

        return d[head]       