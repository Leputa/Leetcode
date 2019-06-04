#include <vector>
using namespace std;

/*
当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]）
另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少（local[i][j]）
全局递推式：
    global[i][j]=max(local[i][j],global[i-1][j])
局部递推式：
    local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)

*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length <= 1)
            return 0;
        vector <vector<int>> global(length);
        for (int i=0; i<length; i++){
            global[i].resize(3);
        }
        vector <vector<int>> local(length);
        for (int i=0; i<length; i++){
            local[i].resize(3);
        }

        for (int i=1; i<length; i++){
            int diff = prices[i] - prices[i-1];
            for (int j=1; j<3; j++){
                local[i][j] = max(local[i-1][j] + diff, global[i-1][j-1] + max(diff, 0));
                global[i][j] = max(local[i][j], global[i-1][j]);
            }
        }
        return global[length-1][2];
    }
};
