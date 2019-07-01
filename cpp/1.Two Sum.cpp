#include <vector>
#include <unordered_map>
#include <iostream>


using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>ret;
        unordered_map<int, int>map;
        for(int i=0; i<nums.size(); i++){
            map[target- nums[i]] = i;
        }
        for (int i=0; i<nums.size(); i++){
            if (map.count(nums[i]) != 0 && map[nums[i]] != i){
                ret.push_back(i);
                ret.push_back(map[nums[i]]);
                break;
            }
        }
        return ret;
    }
};