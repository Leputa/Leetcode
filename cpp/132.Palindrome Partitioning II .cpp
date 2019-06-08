#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int minCut(string s) {
        int length = s.length();
        vector<vector<int>> dp(length);
        for (int i=0; i<length; i++)
            dp[i].resize(length);

        vector<int>cut(length+1); // i到末尾的最小分段数

        for (int i=length-1; i>=0; i--){
            cut[i] = INT_MAX;
            for (int j=i; j<length; j++){
                if ((s[i] == s[j]) && ((j-i <= 1) || (dp[i+1][j-1] == 1))){
                    dp[i][j] = 1;
                    cut[i] = min(cut[j+1]+1, cut[i]);
                }
            }
        }
        return cut[0]-1;
    }
};

