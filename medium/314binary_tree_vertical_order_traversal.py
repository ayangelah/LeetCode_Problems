 # 314 binary tree vertical order traversal

class Node:
    def __init__(self, val, left, right): # didn't specify the structure of node, so decided on this
        self.val = val
        self.left = left
        self.right = right

def vertical_traversal(root):
    # approach: insert either to the beginning or end of the list based on if there are rightmost or leftmost children. There are even and odd rows
    node_dict = {}
    queue = [(root, None, 0)] # list of (node, position of parent, -1 for left +1 for right)
    while queue:
        curr = queue.pop(0)
        index_of_insertion = 0
        if curr[1] is None:
            node_dict[0] = [curr[0].val]
        else:
            if curr[1] + curr[2] in node_dict:
                node_dict[curr[1] + curr[2]].append(curr[0].val)
            else:
                node_dict[curr[1] + curr[2]] = [curr[0].val]
            index_of_insertion = curr[1] + curr[2]
        # add to queue for next iterations
        if curr[0].left is not None:
            queue.append((curr[0].left, index_of_insertion, -1))
        if curr[0].right is not None:
            queue.append((curr[0].right, index_of_insertion, 1))
    
    sorted_keys = list(node_dict.keys())
    sorted_keys.sort()
    solution = []
    for k in sorted_keys:
        solution.append(node_dict[k])
    return solution

def tests():
    #   3
    #  /\
    # /  \
    # 9  20
    #    /\
    #   /  \
    #  15   7
    node7 = Node(7, None, None)
    node15 = Node(15, None, None)
    node20 = Node(20, node15, node7)
    node9 = Node(9, None, None)
    rootnode = Node(3, node9, node20)
    print(vertical_traversal(rootnode))