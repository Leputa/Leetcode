#include <vector>
#include <iostream>
using namespace std;

class Solution {

public:
    vector<vector<int> > FindContinuousSequence(int sum) {
        vector<vector<int> >ret;
        for (int i=1; i<= sum/2+1; i++){
            int tmp_sum = 0;
            vector<int>tmplist;
            for (int j=i; j<= sum/2+1; j++){
                tmp_sum += j;
                tmplist.push_back(j);
                if (tmp_sum > sum) break;
                else if(tmp_sum == sum){
                    cout << "2b" << endl;
                    ret.push_back(tmplist);
                    break;
                }
            }
        }
        return ret;
    }
};


int main(){
    Solution solutino = Solution();
    solutino.FindContinuousSequence(3);
    return 0;
}