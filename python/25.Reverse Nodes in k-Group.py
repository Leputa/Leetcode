# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or k==1 or head==None:
        	return head
        tmp=head
        # h=ListNode(None)
        # for i in range(k):
        # 	nextNode=tmp.next
        # 	tmp.next=h.next
        # 	h.next=tmp
        # 	tmp=nextNode
        # head.next=nextNode
        # return h.next
       	cnt=0
       	while(tmp!=None):
       		cnt+=1
       		tmp=tmp.next
       	if k>cnt:
       		return head
       	newhead=head
       	for i in range(cnt//k):
       		newhead,tail=self.reverseList(newhead,k)
       		if i!=0:
       			oldtail.next=newhead
       		if i==0:
       			returnNode=newhead
       		oldtail=tail
       		newhead=tail.next
       	return returnNode

    def reverseList(self,head,k):
    	if head.next==None:
    		return head
    	tmpNode1=head
    	tmpNode2=tmpNode1.next
    	tail=None
    	for i in range(k-1):
    		tmpNode1.next=tmpNode2.next
    		tmpNode2.next=head
    		head=tmpNode2
    		if i==k-2:
    			tail=tmpNode1
    		tmpNode2=tmpNode1.next
    	return head,tail




head=ListNode(1)
print(Solution().reverseList(head,2).val)