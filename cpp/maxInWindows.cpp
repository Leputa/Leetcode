#include <vector>
#include <queue>
using namespace std;


class Solution {
public:
    vector<int> maxInWindows(const vector<int>& num, unsigned int size)
    {
        vector<int>ret;
        if (size <= 0)
            return ret;

        if (num.size() < size)
            return ret;

        deque<int>q;
        int max_num = -INT_MAX, second_max_num = -INT_MAX;
        for (int i=0; i<size; i++){
            if (num[i] >= max_num)
                max_num = num[i];
            q.push_back(num[i]);
        }
        ret.push_back(max_num);
        for (int i=size; i<num.size(); i++){
            int front_num = q.front();
            q.pop_front();
            q.push_back(num[i]);
            if (front_num == max_num){
                max_num = -INT_MAX;
                for(int j = 0; j < q.size(); j++){
                    if (q.at(j) > max_num)
                        max_num = q.at(j);
                }
            }
            else if (num[i] >= max_num){
                max_num = num[i];
            }
            ret.push_back(max_num);
        }
        return ret;
    }
};

