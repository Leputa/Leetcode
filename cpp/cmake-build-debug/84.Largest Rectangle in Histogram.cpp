#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int>_stack;
        int max_area = 0;
        int i = 0;
        heights.push_back(0);
        while(i < heights.size()){
            if (_stack.empty() || heights[i] > heights[_stack.top()]){
                _stack.push(i);
                i++;
            }
            else{
                int idx = _stack.top();
                _stack.pop();
                if (_stack.empty())
                    max_area = max(max_area, heights[idx] * i);
                else
                    max_area = max(max_area, heights[idx] * (i - _stack.top() - 1));
            }
        }
        return max_area;
    }
};