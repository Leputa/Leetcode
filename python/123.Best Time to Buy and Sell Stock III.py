from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        left_profit = [0] * len(prices)
        right_profit = [0] * len(prices)
        
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            left_profit[i] = max(left_profit[i-1], prices[i] - min_price)

        max_price = prices[len(prices)-1]
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            right_profit[i] = max(right_profit[i+1], max_price - prices[i])

        ret = 0
        for i in range(len(prices)):
            if left_profit[i] + right_profit[i] > ret:
                ret = left_profit[i] + right_profit[i]
        return ret

