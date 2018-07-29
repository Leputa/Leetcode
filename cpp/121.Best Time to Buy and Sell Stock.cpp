#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length==0 || length==1)
        	return 0;
        
        vector<int> buys(length);
        vector<int> sells(length);
        buys[0] = prices[0];
        sells[length-1] = prices[length-1];
        
        for (int i=1; i<length; i++)
			buys[i] = min(buys[i-1], prices[i]);
		for (int i=length-2; i>=0; i--)
			sells[i] = max(sells[i+1], prices[i]);

		int m = 0;
		for (int i=1; i<length; i++){
			if (sells[i]-buys[i] > m)
				m = sells[i] - buys[i];
		}
		return m;
    }
};

int main(){
	Solution s = Solution();
	vector<int>p = {7,6,4,3,1}; //7,6,4,3,1
	cout<<s.maxProfit(p)<<endl;
	return 0;
}
