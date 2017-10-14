import re

class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        lst=re.split('\/',expression)
        newList=[]
        for i in range(len(lst)):
        	if len(lst[i])!=0:
        		if ('+' in lst[i] ):
        			tmplist=re.split('\+',lst[i])
        			newList.append(int(tmplist[0]))
        			newList.append(int(tmplist[1]))
        		elif('-' in lst[i]):
        			if(i==0):
        				newList.append(int(lst[i]))
        			else:
        				tmplist=re.split('\-',lst[i])
        				newList.append(int(tmplist[0]))
        				newList.append(-int(tmplist[1]))
        		else:
        			newList.append(int(lst[i]))

        numerator=newList[0::2]
        denominator=newList[1::2]
        lcm=self.getlcm(denominator)

        ans=0
        for i in range(len(numerator)):
        	numerator[i]=numerator[i]*(lcm//denominator[i])
        	ans+=numerator[i]

        if (ans==0):
        	return "0/1"

        gcd=self.getgcd(abs(ans),lcm)
        ans=ans//gcd
        lcm=lcm//gcd
        return str(ans)+"/"+str(lcm)



    def getlcm(self,lst):
    	ans=1
    	for i in range(len(lst)):
    		tmp=self.getgcd(ans,lst[i])
    		ans=ans*lst[i]//tmp
    	return ans
    
    def getgcd(self,a,b):
    	c=a%b
    	while(c!=0):
    		a=b
    		b=c
    		c=a%b
    	return b


print(Solution().fractionAddition("5/3+1/3"))