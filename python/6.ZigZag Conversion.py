class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==0 or numRows==1:
        	return s
        ans=[]
        partition=2*numRows-2
        originPartition=partition
        for start in range(numRows):
        	i=start
        	while(i<len(s)):
        		if i==start or start!=0:
        			ans.append(s[i])
        		i+=partition
        		if partition!=0:
        			if i<len(s):
        				ans.append(s[i])
        		i+=(originPartition-partition)	
        	partition-=2
        return "".join(ans)


print(Solution().convert("sdfdscffgfg",1))