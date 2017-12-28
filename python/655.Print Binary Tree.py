# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        ans=[]
        m=self.getLevel(root)
        n=2**m-1
        for i in range(m):
        	tmpList=[""]*n
        	ans.append(tmpList)
        ans[0][n//2]=str(root.val)
        if(root.left!=None):
        	self.printBT(root.left,0,n//2-1,1,ans)
        if(root.right!=None):
        	self.printBT(root.right,n//2+1,n-1,1,ans)
        return ans

    def printBT(self,root,start,end,height,ans):
    	ans[height][(start+end)//2]=str(root.val)
    	if(root.left!=None):
    		self.printBT(root.left,start,(start+end)//2-1,height+1,ans)
    	if(root.right!=None):
    		self.printBT(root.right,(start+end)//2+1,end,height+1,ans)
    	return

    def getLevel(self,root):
    	if root==None:
    		return 0
    	return max(self.getLevel(root.left),self.getLevel(root.right))+1

