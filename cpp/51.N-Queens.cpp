# include <iostream>
# include <vector>
# include <string>
using namespace std;


class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> R(n+1);
		vector<int> U(2*n + 1);
		vector<int> D(2*n + 1);
		vector<int> p(n+1);
		vector<vector<string>> result;
		
		for (int i=0; i<n+1; i++)
			R[i] = 0;
		for (int i=0; i<2*n+1; i++){
			U[i] = 0;
			D[i] = 0;
 		}
 		getPosition(1, n, R, U, D, p, result);
 		return result;
    } 
private:
	void getPosition(int col, int n, vector<int>&R, vector<int>&U, vector<int>&D, vector<int>&p, vector<vector<string>> &result){
		if (col == n+1){
			vector<string> tmp(n);
			for (int c=1; c <= n; c++){
				tmp[c-1] = string(n, '.');
				tmp[c-1][p[c]-1] = 'Q';
			}
			result.push_back(tmp);
		}
		for (int row = 1; row <= n; row++){
			if (R[row]==0 && U[col+row]==0 and D[col-row+(n+1)]==0){
				R[row]=1;
				U[col+row]=1;
				D[col-row+(n+1)]=1;
				p[row] = col;               //row和col可以交换，转置矩阵.... 
				getPosition(col+1, n, R, U, D, p, result);
				R[row]=0;
				U[col+row]=0;
				D[col-row+(n+1)]=0;
			}
		}
	}
};
