class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n==0):
        	return 0
        if (n==1):
        	return 1
        s=[1]
        p=[]
        idxP=0
        cnt=1
        i=0
        while(i<n-1):
        	nextS=1
        	if (nextS==s[i]):
        		nextP=2
        		if nextP==s[idxP]:
        			s.append(nextS)
        			p.append(nextP)
        			s.append(2)
        			i+=2
        			idxP+=1
        			cnt+=1
        			continue
        	elif (nextS!=s[i]):
        		nextP=1
        		if nextP==s[idxP]:
        			s.append(nextS)
        			p.append(nextP)
        			idxP+=1
        			cnt+=1
        			i+=1
        			continue
        	nextS=2
        	if (nextS==s[i]):
        		nextP=2
        		if nextP==s[idxP]:
        			s.append(nextS)
        			p.append(nextP)
        			s.append(1)
        			i+=2
        			idxP+=1
        			if(i<n):
        				cnt+=1
        			continue
        	elif (nextS!=s[i]):
        		nextP=1
        		if nextP==s[idxP]:
        			s.append(nextS)
        			p.append(nextP)
        			idxP+=1
        			i+=1
        			continue
        return cnt

print(Solution().magicalString(6))







