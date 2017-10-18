class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        self.combination(ans,[],k,1,n)
        return ans

    def combination(self,ans,tmp,k,start,n):
    	if(len(tmp)==k and n==0):
    		ans.append(tmp[:])
    	for i in range(start,10):
    		tmp.append(i)
    		self.combination(ans,tmp,k,i+1,n-i)
    		tmp.pop()




print(Solution().combinationSum3(4,8))
    		







