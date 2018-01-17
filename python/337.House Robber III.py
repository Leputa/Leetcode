#import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if(root==None):
#         	return 0
#         maxSum=[0]
#         level=0
#         myQueue=queue.Queue()
#         myQueue.put(root)
#         while(myQueue.empty()==False):
#         	level+=1
#         	levelNum=myQueue.qsize()
#         	cnt=0
#         	sum=0
#         	while(cnt<levelNum):
#         		temp=myQueue.get()
#         		sum+=temp.val
#         		if(temp.left!=None):
#         			myQueue.put(temp.left)
#         		if(temp.right!=None):
#         			myQueue.put(temp.right)
#         		cnt+=1
#         	if (level==1):
#         		maxSum.append(sum)
#         	else:
#         		max=0
#         		for i in range(level-1):
#         			if maxSum[i]>max:
#         				max=maxSum[i]
#         		maxSum.append(sum+max)
#         return	maxSum[-1]


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num=self.dfs(root)
        return max(num[0],num[1])    #0 rob this node;1 not rob this node

    def dfs(self,temp):
    	if (temp==None):
    		return [0]*2
    	left=self.dfs(temp.left)
    	right=self.dfs(temp.right)
    	ans=[0]*2
    	ans[0]=left[1]+right[1]+temp.val
    	ans[1]=max(left[0],left[1])+max(right[0],right[1])
    	return ans
