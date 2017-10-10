#include <algorithm>
#include <vector>
#include <stdio.h>
using namespace std;

class Solution {
public:
    int distributeCandies(vector <int> & candies) {
        int cnt=0;
        int kinds=1;
        int brother=0;
        sort(candies.begin(),candies.end());
        for (int i=1;i<candies.size();i++){
        	if(candies[i]==candies[i-1])
        		brother++;		
			else
        		kinds++;		
		}
		if(brother>=candies.size()/2)
			return kinds;
		else
			return candies.size()/2;
    }
};

int main(){
	vector<int> a={5,5,4,7,5,8,5,9,5,2};
	Solution s;
	printf("%d\n",s.distributeCandies(a));
	return 0;
}

