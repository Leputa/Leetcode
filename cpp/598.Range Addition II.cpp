#include <vector>
using namespace std;

class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int minrow=m,mincol=n;
        for (int i=0;i<ops.size();i++){
        	if(ops[i][0]<minrow)
        		minrow=ops[i][0];
		}
		for (int i=0;i<ops.size();i++){
        	if(ops[i][1]<mincol)
        		mincol=ops[i][1];
		}
		return minrow*mincol;
    }
};
