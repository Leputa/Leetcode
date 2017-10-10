class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for i in range(1,len(prices)):
        	if(prices[i]-prices[i-1]>0):
        		profit+=prices[i]-prices[i-1]
        return profit

print(Solution().maxProfit([1,7,5,2,23,34,1,2]))