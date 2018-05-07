class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        length = 0 
        tmpNode = head 
        while (tmpNode!=None):
            tmpNode = tmpNode.next
            length += 1
        
        if length < k:
            return None

        tmpNode = head
        for i in range(length-k):
            tmpNode = tmpNode.next
        return tmpNode