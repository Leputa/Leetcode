#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (accumulate(gas.begin(),gas.end(),0) < accumulate(cost.begin(), cost.end(), 0))
            return -1;
    }
};
