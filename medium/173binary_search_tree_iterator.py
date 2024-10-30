from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        self.addLeft(root)
    
    def addLeft(self, node):
        while node.left is not None:
            self.stack.append(node.left)
            node = node.left

    def next(self) -> int:
        curr_root = self.stack.pop()
        if curr_root.right is not None:
            self.stack.append(curr_root.right)
            self.addLeft(curr_root.right)
        return curr_root.val

    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()