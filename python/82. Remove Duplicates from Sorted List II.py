# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        pHead = ListNode(None)
        pHead.next = head
        pTail = pHead

        tmpNode = head


        while(tmpNode != None):
            pNext = tmpNode.next
            if pNext==None or tmpNode.val != pNext.val:
                pTail.next = tmpNode
                pTail = tmpNode
                tmpNode = pNext
            else:
                while(pNext!=None and pNext.val == tmpNode.val):
                    pNext = pNext.next
                tmpNode = pNext
                if tmpNode == None:
                    pTail.next = tmpNode
                    
        return pHead.next

