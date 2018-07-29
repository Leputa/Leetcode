#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length==0 || length==1)
        	return 0;
        
        int min = prices[0];
        int profit = 0;
        for (int i=1; i<length; i++){
        	if (min>prices[i])
        		min = prices[i];
        	else{
        		profit += prices[i] - min;
        		min = prices[i];
			}
		}
		return profit;
    }
};

int main(){
	Solution s = Solution();
	vector<int>p = {7,1,5,3,6,4}; //7,6,4,3,1
	cout<<s.maxProfit(p)<<endl;
	return 0;
}
