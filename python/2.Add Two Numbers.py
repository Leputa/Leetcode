# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1=self.reverseList(l1)
        l2=self.reverseList(l2)
        a=0
        b=0
        while(l1!=None):
        	a*=10
        	a+=l1.val
        	l1=l1.next
        while(l2!=None):
        	b*=10
        	b+=l2.val
        	l2=l2.next

        ans=a+b
        head=ListNode(ans%10)
        tmpNode=head
        ans/=10
        while(ans!=0):
        	tmpNode.next=ListNode(ans%10)
        	ans/=10
        	tmpNode=tmpNode.next
        return head

    def reverseList(self,head):
    	if head.next==None:
    		return head
    	tmpNode1=head
    	tmpNode2=tmpNode1.next
    	while(tmpNode2!=None):
    		tmpNode1.next=tmpNode2.next
    		tmpNode2.next=head
    		head=tmpNode2
    		tmpNode2=tmpNode1.next
    	return head