class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        i=1
        j=n

        ans=[]

        while(i<=j):
        	if(k!=1):
        		if(k%2==0):
        			ans.append(i)
        			i+=1
        		else:
        			ans.append(j)
        			j-=1
        		k-=1
        	else:
        		ans.append(j)
        		j-=1
        return ans

         