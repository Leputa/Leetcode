import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length=0
        tmp=root
        while(tmp!=None):
        	length+=1
        	tmp=tmp.next
        lenofList=[]
        kk=k
        while(length%kk!=0):
        	num=math.ceil(length/kk)
        	length-=num
        	lenofList.append(num)
        	kk-=1
        start=len(lenofList)
        for i in range(start,k):
        	lenofList.append(length//kk)
        tmp=root
        ans=[]
        for length in lenofList:
        	tmpList=[]
        	while(length>0):
        		tmpList.append(tmp.val)
        		tmp=tmp.next
        		length-=1
        	ans.append(tmpList)
        return ans

root=ListNode(1)
for i in range(10,1,-1):
	node=ListNode(i)
	node.next=root.next
	root.next=node

print(Solution().splitListToParts(root,3))
        