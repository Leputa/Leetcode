# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def swapPairs(self, head):
	    left=head
	    if(left!=None and left.next!=None):
	        right=left.next
	        left.next=right.next
	        right.next=left
	        tail=left
	        left=left.next
	        head=right
	    while (left!=None and left.next!=None):
	        right=left.next
	        left.next=right.next
	        right.next=left
	        tail.next=right
	        tail=left
	        left=left.next
	    return head



