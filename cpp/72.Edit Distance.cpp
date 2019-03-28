# include<string>
# include<vector>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int length1 = word1.size();
        int length2 = word2.size();
        vector<vector<int>> dp(length1+1);
        for(int i=0; i<length1+1; i++)
        	dp[i].resize(length2+1);
        	
        for (int i=0; i<length1+1; i++)
        	dp[i][0] = i;
    	
    	for (int j=0; j<length2+1; j++)
    		dp[0][j] = j;
		
		for(int i=1; i<length1+1; i++){
			for (int j=1; j<length2+1; j++){
				if (word1[i-1] == word2[j-1])
					dp[i][j] = dp[i-1][j-1];
				else
					dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))+1;  //dp[i-1][j-1]： 修改
					                                                              //dp[i][j-1]: 删除word2[j-1]
					                                                              //dp[i-1][j]: 删除word1[i-1]
			}
		}
		return dp[length1][length2];
    }
};
