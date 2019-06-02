#include <vector>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length <= 1)
            return 0;
        vector<int> buys(length);   //第i天或者第i天前买入的最少花费
        vector<int> sells(length);  //第i天或者第i天后卖出的最大收益
        buys[0] = prices[0];
        sells[length-1] = prices[length-1];
        for (int i=1; i<length; i++)
            buys[i] = min(buys[i-1], prices[i]);
        for (int i=length-2; i >= 0; i--)
            sells[i] = max(sells[i+1], prices[i]);
        int max_profit = 0;
        for (int i=0; i<length; i++)
            max_profit = max(max_profit, sells[i] - buys[i]);
        return max_profit;
    }
};