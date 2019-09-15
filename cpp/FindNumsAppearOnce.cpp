#include <vector>
using namespace std;

class Solution {
public:
    void FindNumsAppearOnce(vector<int> data,int* num1,int *num2) {
        int _xor = 0;
        for(auto num: data){
            _xor ^= num;
        }
        int flag = 1;
        // 找出num1和num2不相同的最低位
        while((_xor & flag) == 0){
            flag <<= 1;
        }
        *num1 = _xor, *num2 = _xor;
        for (auto num: data){
            if ((flag & num) == 0)
                *num1 ^= num;
            else
                *num2 ^= num;            
        }
    }
};