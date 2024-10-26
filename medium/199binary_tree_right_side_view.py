from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # traverse in order, and grab the rightmost of each level
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: # edge case
            return []
            
        queue = [(root, 0)]
        levels = []
        while queue:
            curr_node, curr_level = queue.pop(0)
            if curr_node.left is not None:
                queue.append((curr_node.left, curr_level + 1))
            if curr_node.right is not None:
                queue.append((curr_node.right, curr_level + 1))
            if curr_level == len(levels):
                levels.append([curr_node.val])
            else:
                levels[curr_level].append(curr_node.val)
        
        result = []
        for j in range(len(levels)):
            result.append(levels[j][-1])
        return result