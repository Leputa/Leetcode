# include <iostream>
# include <vector>
using namespace std;


class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        if (nums.size() == 2)
        	return nums;
        
		int all = 0;
		for (auto num: nums)
			all ^= num;
		
		int flag = 1;
		while(true){
			if (flag & all) break;       //那两个数字在flag这一位上不相同 
			flag <<= 1;           
		}
		
		//把该vector中的数字分为两类，
		//一类flag位为1，一类flag位为0,然后分别异或处理 
		int res1 = 0, res2 = 0;
		for (auto num: nums){            
			if (num & flag){
				res1 ^= num;
			}
			else res2 ^= num;
		}
		vector <int> result;
		result.push_back(res1);
		result.push_back(res2);
		return result;
    }
};

int main(){
	Solution s = Solution();
	vector <int> nums = {1,2,1,3,2,5};
	vector <int> outputs = s.singleNumber(nums);
	for (int i=0; i<outputs.size(); i++){
		cout << outputs[i] << endl;
	}	
}
