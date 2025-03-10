# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        maxlist = []
        queue = deque([root])

        while queue:
            curr_max = float(\-inf\)
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_max = max(curr_max,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            maxlist.append(curr_max)        
        
        return maxlist