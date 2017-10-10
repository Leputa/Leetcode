class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	list=[]
    	while(n!=0):
    		list.append(n%2)
    		n=n//2
    	length=len(list)
    	while(length!=32):
    		list.append(0)
    		length+=1
    	length-=1
    	ans=0
    	for i in list:
    		if i==1:
    			ans+=2**length
    		length-=1
    	return ans

print(Solution().reverseBits(43261596))
