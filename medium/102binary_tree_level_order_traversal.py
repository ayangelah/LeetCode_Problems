# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        # BFS = queue, with dividers for levels
        queue = [root, None]  # append to end, pop off front
        curr = None
        solution = []
        currlevel = []
        while len(queue) > 1:  # account for last None element
            curr = queue.pop(0)
            if curr == None:  # divider hit, add divider since leftmost node has just been processed in a level
                # print(currlevel)
                queue.append(None)  # next divider
                solution.append(currlevel)
                currlevel = []
                continue  # don't process like normal node """
            if curr.left != None:
                # print("left: ", curr.left.val)
                queue.append(curr.left)
            if curr.right != None:
                # print("right: ", curr.right.val)
                queue.append(curr.right)
            currlevel.append(curr.val)
        solution.append(currlevel)
        return solution
