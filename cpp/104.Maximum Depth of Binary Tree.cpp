#include<stdio.h>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
	int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	int max(int a,int b){
		return a>b?a:b;
	}
	
    int maxDepth(TreeNode* root) {
        if (root->left==NULL&&root->right==NULL)
        	return 1;
        else
        	return 1+max(maxDepth(root->left),maxDepth(root->right));
    }
};
