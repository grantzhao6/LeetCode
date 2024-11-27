# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,s):
            if root == None:
                return 0

            s = s*10+root.val

            if root.left == None and root.right == None:
                return s
            
            return helper(root.left,s)+helper(root.right,s)

        s = 0
        return helper(root,s)

        