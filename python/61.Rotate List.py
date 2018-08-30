# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head

        length = self.expandList(head)
        k = length - k % length
        for i in range(k):
            head = head.next

        tmpNode = head
        for i in range(length-1):
            tmpNode = tmpNode.next
        tmpNode.next = None
        return head

    def expandList(self, head):
        length = 0
        tmpNode = head
        while(tmpNode != None):
            oldNode = tmpNode
            tmpNode = tmpNode.next
            length += 1
        
        p = head
        tmpNode = ListNode(p.val)
        oldNode.next = tmpNode

        for i in range(length-1):
            p = p.next
            tmpNode.next = ListNode(p.val)
            tmpNode = tmpNode.next
        tmpNode.next = None
        
        return length
            
