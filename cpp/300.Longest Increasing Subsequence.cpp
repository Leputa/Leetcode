# include <iostream>
# include <vector>
using namespace std;


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int length = nums.size();
        if (length == 0)
        	return 0;
        vector<int> dp(length, 1);
		int ret = dp[0];
		
		for (int i=1; i<length; i++){
			for (int j=0; j<i; j++){
				if (nums[j] < nums[i]){
					dp[i] = max(dp[i], dp[j]+1);
				}
			}
			if (dp[i] > ret)
				ret = dp[i];
		}
		return ret;	
    }
};
