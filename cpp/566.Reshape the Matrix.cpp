#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
    	int row=nums.size();
    	int col=nums[0].size();
    	if (row*col!=r*c)
    		return nums;
    	vector<vector<int>> ans(r);
    	for (int i=0;i<r;i++)
    		ans[i].resize(c);
    	int ii=0;
    	int jj=0;
    	for (int i=0;i<row;i++){
    		for (int j=0;j<col;j++){
    			ans[ii][jj]=nums[i][j];
    			jj++;
    			if(jj==c){
    				jj=0;
    				ii++;
				}
			}
		}
		return ans;
    }
};

int main(){
	vector<vector<int>> nums={{1,2},{3,4}};
	Solution s;
	s.matrixReshape(nums,1,4);
	return 0;
}
