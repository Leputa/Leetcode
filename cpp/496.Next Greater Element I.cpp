#include <vector>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> ans;
        for (int i=0;i<findNums.size();i++)
        	ans.push_back(search(findNums[i],nums));
        return ans;
        
    }
    int search(int e, vector<int>& nums ){
    	for (int i=0;i<nums.size()-1;i++){
    		if (e==nums[i]){
    			for (int j=i+1;j<nums.size();j++)
    				if (nums[j]>e)
    					return nums[j];
			}
		}
		return -1;
	}
};
