class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<=9:
        	return N
        DigitsList=[]
        while(N!=0):
        	DigitsList.append(N%10)
        	N=N//10
        DigitsList.reverse()
        tag=0
       	ans=0
        for i in range(len(DigitsList)-1):
        	ans*=10
        	if tag==0: 
        		if DigitsList[i]<=DigitsList[i+1]:
        			ans+=DigitsList[i]
        		else:
        			tag=1
        			if (DigitsList[i]==DigitsList[i-1]):
        				count=1
        				while(count<=i and DigitsList[i]==DigitsList[i-count]):
        					count+=1
        				for j in range(count):
        					ans=ans//10
        				ans=ans*10+DigitsList[i]-1
        				for j in range(count-1):
        					ans=ans*10+9
        			else:
        				ans+=DigitsList[i]-1
        	else:
        		ans+=9
        if tag==0:
        	ans=ans*10+DigitsList[len(DigitsList)-1]
        else:
        	ans=ans*10+9
        return ans
        		
print(Solution().monotoneIncreasingDigits(333222))