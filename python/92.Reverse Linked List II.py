# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        tmpNode = head
        Head = ListNode(None)
        Head.next = head
        tailNode = Head
        for i in range(m-1):
            tailNode = tmpNode
            tmpNode = tmpNode.next
        tailNode.next = self.reverseNode(tmpNode, n-m+1)
        return Head.next

    def reverseNode(self, head, k):
        Head = ListNode(None)
        tmpNode = head
        for i in range(k):
            nextNode = tmpNode.next
            tmpNode.next = Head.next
            Head.next = tmpNode
            tmpNode = nextNode
        head.next = tmpNode
        return Head.next








