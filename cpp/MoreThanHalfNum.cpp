#include <vector>
using namespace std;

class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {
        if (numbers.size() == 0)
            return 0;
        int ret = numbers[0];
        int times = 0;
        for(auto num: numbers){
            if (num == ret){
                times += 1;
            }else{
                times -= 1;
                if (times < 0){
                    times = 0;
                    ret = num;
                }
            }
        }
        return times>0?ret:0;      
    }
};