#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 2)
            return 0;
        int max_height = -1;
        int max_index =  -1;
        for (int i=0; i<height.size(); i++){
            if (height[i] > max_height){
                max_index = i;
                max_height = height[i];
            }
        }

        int trap_size = 0;

        int left_height = height[0];
        int right_height = height[height.size()-1];
        for (int i=1; i< max_index; i++){
            if (height[i] < left_height)
                trap_size += left_height - height[i];
            else
                left_height = height[i];
        }
        for (int i=height.size()-2; i>max_index; i--){
            if (height[i] < right_height)
                trap_size += right_height - height[i];
            else
                right_height = height[i];
        }

        return trap_size;
    }
};
