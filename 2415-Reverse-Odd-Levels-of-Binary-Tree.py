# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(left,right,n):
            if left is None or right is None:
                return

            if n%2 == 1:
                left.val, right.val = right.val, left.val
            
            helper(left.left,right.right,n+1)
            helper(left.right,right.left,n+1)
        
        helper(root.left,root.right,1)
        return root



        