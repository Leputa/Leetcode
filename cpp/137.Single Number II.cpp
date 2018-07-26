#include <iostream>
#include <vector>

using namespace std; 

class Solution {
	public:
	    int singleNumber(vector<int>& nums) {
	    	int count[32] = {0};
	    	int result = 0;
	    	int n = nums.size();
	        
	        for (int i=0; i<32; i++){
	        	for (int j=0; j<n; j++){
	        		count[i] += ((nums[j]>>i)&1);
	        		count[i] %= 3;
				}
			} 
			for (int i=0; i<32; i++) 
				result += (count[i]<<i);    //用|=速度要快些，但对我而言不太好理解 
			return result; 
	    }   
};

int main(){
	Solution solution = Solution();
	vector<int>nums = {2, 2, 3, 2};
	cout << solution.singleNumber(nums)<<endl;
	
}
