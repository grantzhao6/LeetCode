# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.mind = float('inf')

        def inorder(root):
            if root == None:
                return
            
            inorder(root.left)

            if self.prev != None:
                self.mind = min(self.mind,root.val-self.prev)
            
            self.prev = root.val

            inorder(root.right)
        
        inorder(root)
        return self.mind



        