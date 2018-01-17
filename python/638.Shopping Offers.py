class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        minCost=999999
        for i in range(len(special)):
        	offer=special[i]
        	self.sub(needs,offer)
        	tag=0
        	for i in needs:
        		if i<0:
        			tag=1
        			break
        	if(tag==0):
        		minCost=min(minCost,self.shoppingOffers(price,special,needs)+offer[-1])
        	self.add(needs,offer)
        cost=0
        for i in range(len(needs)):
        	cost+=price[i]*needs[i]
        return min(cost,minCost)

    def sub(self,needs,offer):
    	for i in range(len(needs)):
    		needs[i]=needs[i]-offer[i]
    def add(self,needs,offer):
    	for i in range(len(needs)):
    		needs[i]=needs[i]+offer[i]

print(Solution().shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))