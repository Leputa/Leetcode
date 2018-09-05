class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        length = self.getLength(head)
        if length == 0 or length == 1:
            return 
        reversehead = self.reverseList(head, length)
        seqNode, reverseNode = head, reversehead
        while(reverseNode != None):
            nextSeqNode = seqNode.next
            nextReverseNode = reverseNode.next
            seqNode.next = reverseNode
            reverseNode.next = nextSeqNode
            seqNode = nextSeqNode
            reverseNode = nextReverseNode


    def getLength(self, head):
        length = 0
        tmpNode = head
        while (tmpNode != None):
            length += 1
            tmpNode = tmpNode.next
        return length


    def reverseList(self, head, length):
        tmpNode = head
        if length % 2 == 0:
            steps = length//2
        else:
            steps = length//2 + 1
        for i in range(steps):
            preNode = tmpNode
            tmpNode = tmpNode.next
        preNode.next = None
        Head = ListNode(None)
        while(tmpNode != None):
            nextNode = tmpNode.next
            tmpNode.next = Head.next
            Head.next = tmpNode
            tmpNode = nextNode
        return Head.next
