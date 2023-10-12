# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# observation: only one path from X to node, via definition of the tree.


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0  # count of good nodes
        # stack for dfs with tuple of node and max val at that node
        stack = [(root, root.val)]
        while len(stack) != 0:
            curr = stack.pop()
            if (curr[0].val >= curr[1]):
                count += 1
            newmax = max(curr[1], curr[0].val)
            if curr[0].left != None:
                stack.insert(0, (curr[0].left, newmax))
            if curr[0].right != None:
                stack.insert(0, (curr[0].right, newmax))
        return count
