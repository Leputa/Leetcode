#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        for (int i=1;i<nums.size();i++)
        	nums[0]^=nums[i];              //����������㽻���ɽ���� 
        return nums[0];
    }
};
