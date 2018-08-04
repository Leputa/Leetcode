#include <vector>
using namespace std;


class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
    	int length = cost.size();
        vector<int>dp(length, 0);
        dp[0] = cost[0];
        dp[1] = cost[1];
        for(int i=2; i<length; i++)
        	dp[i] = min(dp[i-1], dp[i-2]) + cost[i];
    	return min(dp[length-1], dp[length-2]);
    }
};
