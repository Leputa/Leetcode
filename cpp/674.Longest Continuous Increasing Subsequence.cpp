# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
    	int length = nums.size();
    	if (length == 0)
    		return 0;
        vector<int> dp(length, 1);
        int ret = dp[0];
        
        for (int i=1; i<length; i++){
        	if (nums[i] > nums[i-1]){
        		dp[i] = dp[i-1] + 1;
			}
			if (dp[i] > ret)
				ret = dp[i];
		}
		return ret;	 
    }
};
