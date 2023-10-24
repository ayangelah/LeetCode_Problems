# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        """ LIST SOLUTION (accident)
        exp = 0
        sol = 0
        for i in range(len(head)-1, -1, -1):
            if head[i] == 1:
                sol += 2**exp
            exp += 1
        return sol
        """
        # convert to string
        stringy = ""
        curr = head
        while (curr.next != None):
            stringy += str(curr.val)
            curr = curr.next
        stringy += str(curr.val)

        # string sol
        exp = 0
        sol = 0
        for i in range(len(stringy)-1, -1, -1):
            if stringy[i] == "1":
                sol += 2**exp
            exp += 1
        return sol
