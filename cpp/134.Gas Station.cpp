#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (accumulate(gas.begin(),gas.end(),0) < accumulate(cost.begin(), cost.end(), 0))
            return -1;
        int remain = 0;
        int idx = 0;
        for (int i=0; i<gas.size(); i++){
            remain += (gas[i] - cost[i]);
            if (remain < 0){
                idx = i+1;
                remain = 0;
            }
        }
        return idx;
    }
};
