#include <vector>
using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        if (n<=1)
            return n;
        vector<int>nums = {1};
        int i2=0, i3 =0, i5=0;
        for (int i=0; i<n; i++){
            int min_num = min(min(nums[i2]*2, nums[i3]*3), nums[i5]*5);
            nums.push_back(min_num);
            i2 += int(nums[i2] * 2 == min_num);
            i3 += int(nums[i3] * 3 == min_num);
            i5 += int(nums[i5] * 5 == min_num);
        }
        return nums[n-1];
    }
};