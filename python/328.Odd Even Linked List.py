# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if (head==None or head.next==None or head.next.next==None):
        	return head
       	temp=head.next.next
       	oddTail=head      #odd list's tail
       	evenhead=head.next
       	eventail=head.next
       	while(temp!=None):
       		oddTail.next=temp
       		nextTemp=temp.next
       		temp.next=evenhead
       		eventail.next=nextTemp
       		if (nextTemp==None):
       			return head
       		temp=nextTemp.next
       		oddTail=oddTail.next
       		eventail=eventail.next
       	return head



        
