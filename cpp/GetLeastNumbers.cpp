#include <vector>
#include <queue>
using namespace std;


class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        vector<int>ret;
        if(k<=0 || k>input.size())
            return ret;
        priority_queue<int>heap; //大顶堆
        for (long i=0; i<input.size(); i++){
            if (heap.size() < k)
                heap.push(input[i]);
            else{
                if (heap.top() > input[i]){
                    heap.push(input[i]);
                    heap.pop();
                }
            }
        }
        while(!heap.empty()){
            ret.push_back(heap.top());
            heap.pop();
        }
        return ret;
    }
};