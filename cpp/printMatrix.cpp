/*
1 2 3 4 
5 6 7 8
9 10 11 12 
13 14 15 16
*/
#include<vector>
#include <iostream>
using namespace std;

class Solution {
private:
    void get_rotate(vector<vector <int> > matrix, int left, int right, int up, int down, vector<int>&ret){
        if (left > right || up > down)
            return;
        int j = left;
        int i = up;
        for (j=left; j <= right; j++)
            ret.push_back(matrix[i][j]);
        --j;
        for (i = up + 1; i<= down; i++)
            ret.push_back(matrix[i][j]);
        --i;
        if (left == right || up == down)
            return;
        for (j=right-1;j >= left; j--)
            ret.push_back(matrix[i][j]);
        ++j;
        for (i = down-1; i > up; i--)
            ret.push_back(matrix[i][j]);
        ++i;
        get_rotate(matrix, left+1, right-1, up+1, down-1, ret); 
    }
    
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int>ret;
        if (matrix.size() == 0)
            return ret;
        int left = 0, right = matrix[0].size()-1;
        int up = 0, down = matrix.size()-1;
        get_rotate(matrix, left, right, up, down, ret);
        return ret;
    }
};

int main(){
    vector<vector<int>> matrix= {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    Solution solution = Solution();
    solution.printMatrix(matrix);
    return 0;
}