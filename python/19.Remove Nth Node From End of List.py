class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp=head
        cnt=0
        while(tmp!=None):
        	tmp=tmp.next
        	cnt+=1
        pos=cnt-n
        if pos<=0:
        	return head.next

        tmp=head
        pre=head
        for i in range(pos):
        	if i==pos-1:
        		pre=tmp
        	tmp=tmp.next
        pre.next=tmp.next
        tmp.next=None
        return head



