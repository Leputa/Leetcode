#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int>map;
        int ans = 0;
        int sum = 0;
        map[0] = 1;
        for(int num: nums){
            sum += num;
            ans += map[sum - k];
            map[sum]++;
        }
        return sum;
    }
};
