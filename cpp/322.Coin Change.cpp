#include <vector>
using namespace std;


class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (coins.size() == 0 || amount == 0)
            return 0;
        vector<vector<int>>dp(coins.size(), vector<int>(amount+1, INT_MAX-100));  // 防溢出
        for (int i=0; i<coins.size();i++)
            dp[i][0] = 0;
        for (int j = 1; j <= amount; j++) {
            if (j >= coins[0]){
                dp[0][j] = min(dp[0][j - coins[0]] + 1, dp[0][j]);
            }
        }
        for (int i=1; i<coins.size(); i++){
            for (int j = 1; j <= amount; j++)
                if (j >= coins[i])
                    dp[i][j] = min(dp[i][j-coins[i]] + 1, dp[i-1][j]);
                else
                    dp[i][j] = dp[i-1][j];
        }
        return dp[coins.size()-1][amount] == INT_MAX-100 ? -1 : dp[coins.size()-1][amount];
    }
};