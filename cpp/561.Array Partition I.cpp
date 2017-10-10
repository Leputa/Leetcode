#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
    	sort(nums.begin(),nums.end());
    	int n=nums.size()/2;
    	int ans=0;
    	for(int i=0;i<2*n;i+=2){
    		ans+=nums[i];
		}
        return ans;
    }
};

