# include <iostream>
using namespace std;

class Solution {
public:
    int totalNQueens(int n) {
        int R[n+1];
		int U[2*n + 1];
		int D[2*n + 1];
		for (int i=0; i<n+1; i++)
			R[i] = 0;
		for (int i=0; i<2*n+1; i++){
			U[i] = 0;
			D[i] = 0;
 		}
		int cnt = 0; 
		return getCounts(cnt, 1, R, U, D, n);
    }
private:
	int getCounts(int cnt, int col, int R[], int U[], int D[], int n){
		if (col == n+1){
			++cnt;
			return cnt;
		}
		for (int row = 1; row <= n; row++){
			if (R[row]==0 && U[col+row]==0 and D[col-row+(n+1)]==0){
				R[row]=1;
				U[col+row]=1;
				D[col-row+(n+1)]=1;
				cnt = getCounts(cnt, col+1, R, U, D, n);
				R[row]=0;
				U[col+row]=0;
				D[col-row+(n+1)]=0;
			}
		}
		return cnt;
	}
};
