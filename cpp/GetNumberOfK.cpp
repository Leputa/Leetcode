#include <vector>
#include <iostream>
using namespace std;

class Solution {
private:
    int getFirstK(vector<int>data, int k){
        int left = 0, right = data.size()-1;
        while(left <= right){
            int mid = left + (right-left)/2;
            if (data[mid] == k){
                if (mid == 0 || data[mid-1] != k)
                    return mid;
                else
                    right = mid-1;
            }
            else if (data[mid] < k)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;
    }
    
    int getLastK(vector<int>data, int k){
        int left = 0, right = data.size()-1;
        while(left <= right){
            int mid = left + (right-left)/2;
            if (data[mid] == k){
                if (mid == data.size()-1 || data[mid+1] != k)
                    return mid;
                else
                    left = mid+1;
            }
            else if (data[mid] < k)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;
    }
public:
    int GetNumberOfK(vector<int> data ,int k) {
        int fisrt_pos = getFirstK(data, k);
        int last_pos = getLastK(data, k);
        return fisrt_pos==-1?0:last_pos-fisrt_pos+1;
    }
};


int main(){
    int k = 3;
    vector<int> data = {1, 2, 3, 3, 3, 3, 4, 5};
    Solution solution = Solution();
    cout << solution.GetNumberOfK(data, k) << endl;
}