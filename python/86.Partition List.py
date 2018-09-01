# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        tmpNode = head

        s_head = ListNode(None)
        b_head = ListNode(None)
        s_tmpNode = s_head
        b_tmpNode = b_head

        while(tmpNode != None):
            if tmpNode.val < x:
                s_tmpNode.next = ListNode(tmpNode.val)
                s_tmpNode = s_tmpNode.next
            else:
                b_tmpNode.next = ListNode(tmpNode.val)
                b_tmpNode = b_tmpNode.next
            tmpNode = tmpNode.next

        s_tmpNode.next = b_head.next
        return s_head.next



