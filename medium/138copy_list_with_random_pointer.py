
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterate through next pointers to build new list
        # build dict of memory location of each old node memory location as key and the new corresponding node
        if head is None:
            return None

        new_root = Node(head.val, None, None)
        node_dict = {id(head): new_root}
        curr_node = head
        curr_new_node = new_root
        while curr_node.next is not None:
            # create new node
            temp = Node(curr_node.next.val, None, None)
            curr_new_node.next = temp
            # update the nodes to next
            curr_new_node = curr_new_node.next
            curr_node = curr_node.next
            # update dictionary
            node_dict[id(curr_node)] = curr_new_node
        
        # set randoms
        curr_node = head
        curr_new_node = new_root
        while curr_node is not None:
            if curr_node.random is not None:
                curr_new_node.random = node_dict[id(curr_node.random)]
            curr_new_node = curr_new_node.next
            curr_node = curr_node.next
        
        return new_root