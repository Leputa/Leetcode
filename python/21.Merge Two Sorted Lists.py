
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1==None):
        	return l2
        if (l2==None):
        	return l1
        
        tmp1=l1
        tmp2=l2

        if tmp1.val<=tmp2.val:
        	head=ListNode(tmp1.val)
        	tmp1=tmp1.next
        elif tmp1.val>tmp2.val:
        	head=ListNode(tmp2.val)
        	tmp2=tmp2.next
        prior=head
        while(tmp1!=None and tmp2!=None):
        	while (tmp1!=None and tmp2!=None) and tmp1.val<=tmp2.val:
        		tmp=ListNode(tmp1.val)
        		prior.next=tmp
        		prior=tmp
        		tmp1=tmp1.next
        	while (tmp1!=None and tmp2!=None) and tmp1.val>tmp2.val:
        		tmp=ListNode(tmp2.val)
        		prior.next=tmp
        		prior=tmp
        		tmp2=tmp2.next
        if (tmp1!=None):
        	prior.next=tmp1
        if (tmp2!=None):
        	prior.next=tmp2

        return head

