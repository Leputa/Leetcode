class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        m=len(prices)
        buy=[0]*(m+1)
        sell=[0]*(m+1)

        buy[0]=-9999999999

        for i in range(1,m+1):
        	buy[i]=max(buy[i-1],sell[i-1]-prices[i-1]-fee)    #什么都不做/买股票
        	sell[i]=max(sell[i-1],buy[i-1]+prices[i-1])       #什么都不做/卖股票
        return sell[m]
