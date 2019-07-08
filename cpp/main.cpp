#include <iostream>
#include <string>
#include <vector>
#include "18.4Sum.cpp"

using namespace std;

int main() {
    Solution solution = Solution();
    vector<int>nums = {1,0,-1,0,-2,2};
    int target = 0;
    solution.fourSum(nums, target);
}