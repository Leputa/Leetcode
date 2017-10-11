# Definition for singly-linked list.
import random

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        
    # def getRandom(self):
    #     """
    #     Returns a random node's value.
    #     :rtype: int
    #     """
    #     length=self.getLength()
    #     step=random.randint(0,length)-1
    #     tmpNode=self.head
    #     for i in range(step):
    #         tmpNode=tmpNode.next
    #     return tmpNode.val

    # def getLength(self):
    #     length=0
    #     tmpNode=self.head
    #     while(tmpNode!=None):
    #         length+=1
    #         tmpNode=tmpNode.next
    #     return length
    def getRandom(self):
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:  #保留当前数据的概率是 1/index
                result = node        
            node = node.next
            index += 1
        return result.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()