class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq=PriorityQueue()
        head=ListNode(None)     #常见的建立头结点的方法
        tmp=head
        for index,listNode in enumerate(lists):
        	if listNode!=None:
        		pq.put((listNode.val,index,listNode))
        while(pq.qsize()>0):
        	tt=pq.get()
        	tmpNode,index=tt[2],tt[1]
        	tmp.next=tmpNode
        	tmp=tmp.next
        	tmpNode=tmpNode.next
        	if tmpNode!=None:
        		pq.put((tmpNode.val,index,tmpNode))
        return head.next








