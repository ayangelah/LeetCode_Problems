# 10/9

# Problem: organization chart of people, boss, employee hierarchy,
# confidential info, some quota to meet. People don't want others to
# see their quotas. Up the management chain can see your quota. Everyone
# has one. Org chart, give list of all people who can view quota,
# including yourself.

# Initial thoughts:
# doubly linked tree, trace upwards until there are no parents.

# traverse tree structure hw.

# Tree Node object
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):  # constructor
        self.val = val
        self.left = left
        self.right = right

# Tree traversal:


class Tree(object):
    # DFS:
    # inorder:
    def inorder(self, root):  # left self right
        if root == None:
            return []
        else:
            return self.inorder(root.left) + [self.value] + self.inorder(root.right)

    # preorder:
    def preorder(self, root):  # self left right
        if root == None:
            return []
        else:
            return [self.value] + self.inorder(root.left) + self.inorder(root.right)

    # postorder:
    def postorder(self, root):  # left right self
        if root == None:
            return []
        else:
            return self.inorder(root.left) + self.inorder(root.right) + [self.value]

    # level order:

    # boundary traversal:

    # diagonal traversal:
