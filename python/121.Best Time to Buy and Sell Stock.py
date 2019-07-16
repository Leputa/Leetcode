class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buys = [0] * len(prices)
        sells = [0] * len(prices)
        buys[0] = prices[0]
        sells[len(prices)-1] = prices[len(prices)-1]
        for i in range(1, len(prices)):
            buys[i] = min(prices[i], buys[i-1])
        for i in range(len(prices)-2, -1, -1):
            sells[i] = max(prices[i], sells[i+1])
        ret = 0
        for i in range(len(prices)):
            if (sells[i] - buys[i] > ret):
                ret = sells[i] - buys[i]
        return ret