#include <vector>
using namespace std;

class Solution {
public:
    int GetUglyNumber_Solution(int index) {
        if (index <= 0)
            return 0;
        if (index == 1)
            return 1;

        vector<int>nums = {1};
        int i2 = 0, i3 = 0, i5 = 0;
        for (int i=2; i<=index; i++){
            int num2 = 2 * nums[i2], num3 = 3 * nums[i3], num5 = 5 * nums[i5];
            int minNum = min(num5, min(num2, num3));
            nums.push_back(minNum);
            i2 += int(minNum == num2);
            i3 += int(minNum == num3);
            i5 += int(minNum == num5);
        }
        return nums[nums.size()-1];
    }
};

