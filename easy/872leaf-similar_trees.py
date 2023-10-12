# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafseq(root1) == self.leafseq(root2)

    def leafseq(self, root):
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            return self.leafseq(root.left) + self.leafseq(root.right)
