#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>>ret;
        if (nums.size() < 4)
            return ret;

        sort(nums.begin(), nums.end());
        unordered_map<int, int>map;

        vector<int> tmpVec;
        findNsum(nums, target, tmpVec, ret, 0, 4);
        return ret;
    }

private:
    void findNsum(vector<int>& nums, int target, vector<int>&tmpVec, vector<vector<int>> &ret, int start, int N){
        if (N == 2){
            int left = start;
            int right = nums.size() - 1;
            while(left < right){
                int diff = nums[left] + nums[right] - target;
                if (diff == 0){
                    tmpVec.push_back(nums[left]);
                    tmpVec.push_back(nums[right]);
                    ret.push_back(tmpVec);  //cpp居然是深度复制
                    tmpVec.pop_back();
                    tmpVec.pop_back();
                    ++left;
                    while(left < right && nums[left-1] == nums[left]) ++left;
                    --right;
                    while(left < right && nums[right + 1] == nums[right]) --right;
                }
                else if(diff > 0){
                    --right;
                    while(left < right && nums[right + 1] == nums[right]) --right;
                }
                else{
                    ++left;
                    while(left < right && nums[left-1] == nums[left]) ++left;
                }
            }
            return;
        }
        for (int i=start; i<nums.size()-N+1; i++){
            if (nums[i] * N > target or nums[nums.size()-1] * N < target)
                break;
            if (i > start && nums[i] == nums[i-1])
                continue;

            tmpVec.push_back(nums[i]);
            findNsum(nums, target-nums[i], tmpVec, ret, i+1, N-1);
            tmpVec.pop_back();
        }
    }
};

