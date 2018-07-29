# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
    	int length = nums.size();
    	if (length == 0)
    		return 0;
    	if (length == 1)
    		return nums[0];
        vector<int> dp(length);
        vector<int> dp_0(length);
        
        dp[0] = nums[0];
        dp[1] = nums[1];
        
        dp_0[0] = 0;
        dp_0[1] = nums[1];
        
        for (int i=2; i<length; i++){
			int m = 0;
			int m_0 = 0;
			if (i != length-1){
				for (int j=0; j<=i-2; j++){
					if (dp[j] > m)
						m = dp[j];
					if (dp_0[j] > m_0){
						m_0 = dp_0[j];
					}
				}
        		dp[i] = max(m + nums[i], dp[i-1]);
        		dp_0[i] = max(m_0 + nums[i], dp_0[i-1]);
			}
			else {
				for (int j=1; j<=i-2; j++){
					if (dp_0[j] > m)
						m = dp_0[j];
				}
				dp_0[i] = max(m+nums[i], dp_0[i-1]);
				dp[i] = max(dp_0[i], dp[i-1]);
			}

    	}
		int max = 0;
        for (int i=0; i<length; i++){
        	if (dp[i] > max)
        		max = dp[i];
		} 
		return max;
    }
};
