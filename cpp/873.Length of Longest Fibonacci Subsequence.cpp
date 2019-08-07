#include <vector>
#include <unordered_map>

using namespace std;


class Solution {
public:
    int lenLongestFibSubseq(vector<int>& A) {
        /*
         f[i, j] = f[j-i, i] + 1
         */
        int length = A.size();
        if (length < 3)
            return 0;

        vector<vector<int>>dp(length);
        for (int i = 0; i < length; i++)
            dp[i].resize(length);

        unordered_map<int, int>map;
        for (int i = 0; i < length; i++)
            map[A[i]] = i;

        int ret = 0;
        for (int i=0; i<length-1; i++){
            for (int j = i+1; j<length; j++){
                dp[i][j] = 2;
                if (map.find(A[j]-A[i]) != map.end()){
                    int key = map[A[j]-A[i]];
                    dp[i][j] = max(dp[key][i] + 1, dp[i][j]);
                }
                if (dp[i][j] > ret)
                    ret = dp[i][j];
            }
        }

        return ret == 2? 0:ret;
    }
};