# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        total_swaps = 0

        def get_min_swaps(l):
            swaps = 0
            target = sorted(l)

            pos = {val : idx for idx,val in enumerate(l)}

            for i in range(len(l)):
                if l[i] != target[i]:
                    swaps += 1

                    cur_pos = pos[target[i]]
                    pos[l[i]] = cur_pos
                    l[cur_pos] = l[i]
            
            return swaps

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            total_swaps += get_min_swaps(level_values)
        
        return total_swaps

            

        