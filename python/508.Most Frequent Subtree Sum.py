# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

dic={}

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[] 
        if root==None:
        	return ans
        
        global dic
        self.getDic(root)
        
        max=0
        for i in dic:
        	if dic[i]>max:
        		max=dic[i]
        		ans=[]
        		ans.append(i)
        	elif dic[i]==max:
        		ans.append(i)
        return ans

    
    def getDic(self,tmp):
        global dic
        tmpSum=self.getSum(tmp)
        dic[tmpSum]=dic.get(tmpSum,0)+1
        if (tmp.left!=None):
        	self.findFrequentTreeSum(tmp.left)
        if (tmp.right!=None):
        	self.findFrequentTreeSum(tmp.right)

    def getSum(self,tmp):
    	sum=0
    	stack=[]

    	while(tmp!=None or len(stack)!=0):
    		while(tmp!=None):
    			stack.append(tmp)
    			tmp=tmp.left
    		if (len(stack)!=None):
    			tmp=stack.pop()
    			sum+=tmp.val
    			tmp=tmp.right
    	return sum

root=TreeNode(5)
leftNode=TreeNode(2)
rightNode=TreeNode(-3)
root.left=leftNode
root.right=rightNode

print(Solution().findFrequentTreeSum(root))





