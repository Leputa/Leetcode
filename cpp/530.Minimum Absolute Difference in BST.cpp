#include <iostream>
#include <limits.h>
#include <cmath>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
	private:
		vector<int> valNum;
	public:
		void inOrder(TreeNode *root){
			if(root==NULL)
				return;
			if(root->left)
				inOrder(root->left);
			valNum.push_back(root->val);
			if(root->right)
				inOrder(root->right);
		}
		
		
		int getMinimumDifference(TreeNode* root) {
        	inOrder(root);
        	int len=valNum.size();
        	int minNum=INT_MAX;
        	for (int i=1;i<len;i++){
        		if(valNum[i]-valNum[i-1]<minNum)
        			minNum=valNum[i]-valNum[i-1];
			}
			return minNum;
    	}
};
