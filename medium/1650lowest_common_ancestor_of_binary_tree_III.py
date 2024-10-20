# lowest common ancestor of a binary tree

class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def LCA(p, q):
    # make a set of ancestors encountered, check if ancestor has been encountered
    p_ancestor = p
    q_ancestor = q
    p_ancestor_set = set()
    q_ancestor_set = set()
    while True:
        if p_ancestor in q_ancestor_set:
            return p_ancestor
        elif q_ancestor in p_ancestor_set:
            return q_ancestor
        p_ancestor_set.add(p_ancestor)
        q_ancestor_set.add(q_ancestor)
        if p_ancestor.parent is None and q_ancestor.parent is None:
            return None
        if p_ancestor.parent is not None:
            p_ancestor = p_ancestor.parent
        if q_ancestor.parent is not None:
            q_ancestor = p_ancestor.parent

def tests():
    #.     1
    #.   2.  3
    #.  4
    node1 = Node(1, None, None, None)
    node2 = Node(2, None, None, node1)
    node3 = Node(3, None, None, node1)
    node4 = Node(4, None, None, node2)
    assert(LCA(node4, node3).val == 1)
    print("all test cases passed")