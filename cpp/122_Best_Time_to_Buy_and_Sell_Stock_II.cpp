#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length <= 1)
            return 0;

        int profit = 0;
        int min_sells_prices = prices[0];
        for (int i = 1; i < length; i++){
            if (prices[i] < min_sells_prices)
                min_sells_prices = prices[i];
            else{
                profit += prices[i] - min_sells_prices;
                min_sells_prices = prices[i];
            }
        }

        return profit;
    }
};

