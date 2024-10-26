
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # iterate down BST to find running sum
        queue = [root]
        curr_sum = 0
        while queue:
            curr_node = queue.pop()
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
            if curr_node.val >= low and curr_node.val <= high:
                curr_sum += curr_node.val
        return curr_sum