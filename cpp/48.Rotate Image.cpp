#include <vector>
using namespace std;


class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int low = 0;
        int high = matrix.size()-1;
        int tmp;
        while(high - low >= 1){
            for (int i=low; i<high; i++){
                tmp = matrix[low][i];
                matrix[low][i] = matrix[high-i+low][low];
                matrix[high-i+low][low] = matrix[high][high-i+low];
                matrix[high][high-i+low] = matrix[i][high];
                matrix[i][high] = tmp;
            }
            --high;
            ++low;
        }
    }
};
