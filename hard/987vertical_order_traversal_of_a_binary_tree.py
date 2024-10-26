from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result_dict = {}
        curr_col_level = {} # key: col, value: list for this level
        queue = [(root, 0, 0)]
        last_level = 0
        while queue:
            curr_node, curr_col, curr_level = queue.pop(0)
            if curr_level != last_level: # process a level
                for item in curr_col_level.items():
                    if item[0] not in result_dict:
                        result_dict[item[0]] = sorted(item[1])
                    else:
                        result_dict[item[0]] += sorted(item[1])
                curr_col_level.clear()
                curr_col_level[curr_col] = [curr_node.val]
                last_level = curr_level
            else:
                if curr_col not in curr_col_level:
                    curr_col_level[curr_col] = [curr_node.val]
                else:
                    curr_col_level[curr_col].append(curr_node.val)
            if curr_node.left is not None:
                queue.append((curr_node.left, curr_col - 1, curr_level + 1))
            if curr_node.right is not None:
                queue.append((curr_node.right, curr_col + 1, curr_level + 1))
        # last level
        for item in curr_col_level.items():
            if item[0] not in result_dict:
                result_dict[item[0]] = sorted(item[1])
            else:
                result_dict[item[0]].extend(sorted(item[1]))
        
        sorted_items = sorted(result_dict.items(), key=lambda x: x[0])
        print(sorted_items)
        return list(map(lambda y: y[1], sorted_items))
