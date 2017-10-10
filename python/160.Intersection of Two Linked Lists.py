class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1=0
        len2=0

        tmp=headA
        while(tmp!=None):
        	tmp=tmp.next
        	len1+=1
        tmp=headB
        while(tmp!=None):
        	tmp=tmp.next
        	len2+=1

        if(len1>len2):
        	tmpA=headA
        	tmpB=headB
        	dis=len1-len2
        	while(dis>0):
        		dis-=1
        		tmpA=tmpA.next
        	while(tmpA!=None and tmpA!=tmpB):
        		tmpA=tmpA.next
        		tmpB=tmpB.next
        	return tmpA
        else:
        	tmpA=headA
        	tmpB=headB
        	dis=len2-len1
        	while(dis>0):
        		dis-=1
        		tmpB=tmpB.next
        	while(tmpA!=None and tmpA!=tmpB):
        		tmpA=tmpA.next
        		tmpB=tmpB.next
        	return tmpA



        