#include <vector>
#include <map>

using namespace std;


class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {

        // sort(nums.begin(), nums.end());
        map<int, int>_map;
        map<int, int>:: iterator upper_iter, lower_iter;
        int dist = INT_MAX;
        int ret;

        for (int i = 0; i<nums.size(); i++)
            _map[nums[i]] = 0;
        for (int i = 0; i<nums.size(); i++)
            _map[nums[i]] ++;

        for (int i = 0; i<nums.size()-1; i++){
            _map[nums[i]]--;
            for (int j=i+1; j < nums.size(); j++){
                _map[nums[j]]--;
                int residual = target - (nums[i] + nums[j]);
                upper_iter = _map.upper_bound(residual);
                if (upper_iter !=  _map.end() && _map[upper_iter->first] != 0){
                    int diff = upper_iter->first - residual;
                    if (diff == 0)
                        return target;
                    if (diff < dist) {
                        dist = diff;
                        ret = target + diff;
                    }
                }
                lower_iter = _map.lower_bound(residual);
                if (lower_iter != _map.end() && _map[lower_iter->first] != 0){

                    int diff = residual - lower_iter->first;
                    if (diff == 0)
                        return target;

                    if (diff < dist){
                        dist = diff;
                        ret = target - diff;
                    }
                }
                _map[nums[j]]++;
            }
            _map[nums[i]]++;
        }
        return ret;
    }
};