# include <vector>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<long>>dp(m);
        for (int i=0; i<m; i++)
            dp[i].resize(n);
        for (int i=0; i<m; i++){
            if (i==0)
                dp[i][0] = grid[i][0];
            else
                dp[i][0] = dp[i-1][0] + grid[i][0];
            for (int j=0; j<n; j++){
                if (j == 0)
                    dp[0][j] = grid[0][j];
                else
                    dp[0][j] = dp[0][j-1] + grid[0][j];
                if (i != 0 and j!=0)
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
};