#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>>ret;
        int i = 0;
        while(i < intervals.size()){
            vector<int>tmp_vec;
            tmp_vec.push_back(intervals[i][0]);
            int j = i+1;
            int end = intervals[i][1];
            while(j < intervals.size() && intervals[j][0] <= end){
                if (intervals[j][1] > end)
                    end = intervals[j][1];
                ++j;
            }
            tmp_vec.push_back(end);
            ret.push_back(tmp_vec);
            i = j;
        }
        return ret;
    }
};
