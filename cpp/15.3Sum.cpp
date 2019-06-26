#include <vector>
#include <unordered_map>
#include <unordered_set>


using namespace std;


//class Solution {
//public:
//    vector<vector<int>> threeSum(vector<int>& nums) {
//        vector<vector<int>>ret;
//        if (nums.size() < 3)
//            return ret;
//
//        unordered_map<int, vector<int>> dict;
//        //unordered_map<int, vector<int>>::iterator it;
//        unordered_set<unordered_set<int>>dul_set;
//
//        for (int i=0; i<nums.size()-1; i++){
//            for (int j = i+1; j<nums.size(); j++){
//                if (dict.find(-nums[j])!= dict.end()){
//                    vector<int> indexes = dict[-nums[j]];
//                    unordered_set<int> tmpSet = {nums[indexes[0]], nums[indexes[1]], nums[j]};
//                    if (dul_set.count(tmpSet) == 0 ){
//                        dul_set.insert(tmpSet);
//                        vector<int> tmpList = {nums[indexes[0]], nums[indexes[1]], nums[j]};
//                        ret.push_back(tmpList);
//                    }
//                }
//                int key = nums[i] + nums[j];
//                vector<int> val = {i, j};
//                dict[key] = val;
//            }
//        }
//        return ret;
//    }
//};
// 上述解法超时

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector <vector<int>>  ret;
        if (nums.size() < 3)
            return ret;

        sort(nums.begin(), nums.end());
        if (nums[0] > 0 || nums[nums.size() - 1] < 0)
            return ret;

        for (int i = 0; i < nums.size()-1; i++){
            if (nums[i] > 0)
                break;
            while(i > 0 && i < nums.size()-1 && nums[i] == nums[i-1])
                i ++;
            int j = i + 1;
            int k = nums.size() - 1;
            int target = -nums[i];

            while(j < k){
                if (nums[j] + nums[k] == target){
                    vector<int>tmp = {nums[i], nums[j], nums[k]};
                    ret.push_back(tmp);
                    j++;
                    while(nums[j] == nums[j-1] && j < k) j++;
                    k--;
                    while(nums[k] == nums[k+1] && j < k) k--;
                }
                else if (nums[j] + nums[k] < target){
                    j++;
                    while(nums[j] == nums[j-1] && j < k) j++;
                }
                else{
                    k--;
                    while(nums[k] == nums[k+1] && j < k) k--;
                }

            }
        }
        return ret;
    }
};