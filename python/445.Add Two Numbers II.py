# -*- coding: utf-8 -*

#Definition for singly-linked list.
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
        if (l1==None):
        	return l2
        if (l2==None):
        	return l1

        tmp1=l1
        length1=0
        tmp2=l2
        length2=0
        while(tmp1!=None):
        	length1+=1
        	tmp1=tmp1.next
        while(tmp2!=None):
        	length2+=1
        	tmp2=tmp2.next

        head1=self.reverseList(l1)
        head2=self.reverseList(l2)
        tmp1=head1.next
        tmp2=head2.next

        if(length1>length2):
        	self.runCombine(tmp1,tmp2)
        	head1=self.reverseList(tmp1)
        	return head1.next
        else:
        	self.runCombine(tmp2,tmp1)
        	head2=self.reverseList(tmp2)
        	return head2.next

    def runCombine(self,l1,l2): #l1比l2长
    	tmp1=l1
    	tmp2=l2
    	tag=0
    	while(tmp2!=None):
    		if (tag==0):
    			tmp1.val=tmp1.val+tmp2.val
    		if (tag==1):
    			tmp1.val=tmp1.val+tmp2.val+1
    		tag=0
    		if(tmp1.val>9):
    			tmp1.val-=10
    			if(tmp1.next==None):
    				tail=ListNode(1)
    				tmp1.next=tail
    				return
    			tag=1
    		tmp1=tmp1.next
    		tmp2=tmp2.next
    	if tag==0:
    		return 
    	while(tag==1 ):
    		tmp1.val=tmp1.val+1
    		if(tmp1.val>9):
    			tmp1.val=tmp1.val-10
    			tag=1
    			if(tmp1.next!=None):
    				tmp1=tmp1.next
    			else:
    				tail=ListNode(1)
    				tmp1.next=tail
    				return
    		else:
    			return

    def reverseList(self,l1):
    	head=ListNode(0) #建立头节点便于操作

    	tmp1=l1.next
    	l1.next=None
    	head.next=l1

    	while(tmp1!=None):
    		tmp2=tmp1.next
    		tmp1.next=head.next
    		head.next=tmp1
    		tmp1=tmp2
    	return head









