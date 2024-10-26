from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # approach: recursive solution in which each frame returns the components of a diameter that goes through that root, and we keep track of a global max
        result = self.recursive_diameter(root)
        return self.diameter

    def recursive_diameter(self, root):
        # returns tuple (left, right)
        if root == None:
            return (-1, -1) # negative because this is one level under a node with 0 diameter, the root itself doesn't exist yet.
        else:
            curr_diameter = (max(self.recursive_diameter(root.left)) + 1, max(self.recursive_diameter(root.right)) + 1)
            print(root.val, curr_diameter)
            if curr_diameter[0] + curr_diameter[1] > self.diameter:
                self.diameter = curr_diameter[0] + curr_diameter[1]
            return curr_diameter