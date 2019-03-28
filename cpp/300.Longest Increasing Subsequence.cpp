# include <iostream>
# include <vector>
using namespace std;


//class Solution {
//public:
//    int lengthOfLIS(vector<int>& nums) {
//        int length = nums.size();
//        if (length == 0)
//        	return 0;
//        vector<int> dp(length, 1);
//		int ret = dp[0];
//
//		for (int i=1; i<length; i++){
//			for (int j=0; j<i; j++){
//				if (nums[j] < nums[i]){
//					dp[i] = max(dp[i], dp[j]+1);
//				}
//			}
//			if (dp[i] > ret)
//				ret = dp[i];
//		}
//		return ret;
//    }
//};
// O(N**2)

class Solution {
public:
	int lengthOfLIS(vector<int>& nums) {
		if (nums.size() == 0)
			return 0;
		vector<int> LIS(nums.size());
		LIS[0] = nums[0];
		int len = 0;
		for (int i=1; i<nums.size(); i++) {
			if (nums[i] > LIS[len]){
				++len;
				LIS[len] = nums[i];
			}
			else{
				int pos = binarySearch(LIS, nums[i], len);
				// LIS[pos-1] < nums[i] < LIS[pos]
				LIS[pos] = nums[i];
			}
		}
		return len + 1;
	}
private:
	int binarySearch(vector<int>& LIS, int target, int right){
		int left = 0;
		int mid;
		while(left < right){
			mid = (left + right) / 2;
			if (LIS[mid] < target)
				left = mid + 1;
			else
				right = mid;
		}
		return left;
	}
};