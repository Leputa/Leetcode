class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        cur=1
        for i in range(1,n+1):
        	ans.append(cur)
        	if cur*10<=n:
        		cur*=10
        	elif cur%10!=9 and cur<n:
        		cur+=1
        	elif cur%10==9 and cur<=n:
        		cur+=1
        		while(cur%10==0):
        			cur//=10
        	else:
        		if(cur>=10):
        			cur//=10
        			if(cur%10==9):
        				cur+=1
        				while(cur%10==0):
        					cur//=10
        			else:
        				cur+=1
        return ans


print(Solution().lexicalOrder(199))
