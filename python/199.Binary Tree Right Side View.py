

import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        if root==None:
        	return ans
        temp=root
        Q=queue.Queue()
        Q.put(temp)
        while(not Q.empty()):
        	curLevelSize=Q.qsize()
        	cnt=0
        	while(cnt<curLevelSize):
        		temp=Q.get()
        		if cnt==curLevelSize-1:
        			ans.append(temp.val)
        		cnt+=1
        		if (temp.left!=None):
        			Q.put(temp.left)
        		if (temp.right!=None):
        			Q.put(temp.right)
        return ans 
