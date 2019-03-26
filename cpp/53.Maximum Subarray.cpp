# include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if (n == 0){
            return 0;
        }
        int ret = -INT_MAX;
        int sum = 0;
        for (int i = 0; i < n; i++){
            sum += nums[i];
            if (sum > ret)
                ret = sum;
            if (sum < 0)
                sum = 0;
        }
        return ret;
    }
};

