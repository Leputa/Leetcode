class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        tmpList=[]
       	self.dfs(1,n,k,res,tmpList)
       	return res

    def dfs(self,start,end,k,res,tmpList):
    	if(len(tmpList)==k):
    		res.append(tmpList[:])
    		return
    	for i in range(start,end+1):
    		tmpList.append(i)
    		self.dfs(i+1,end,k,res,tmpList)
    		tmpList.pop()

    	

print(Solution().combine(4,3))