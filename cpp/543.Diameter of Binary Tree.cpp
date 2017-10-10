#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int m=0;
 
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
    	int temp;
    	if (root==NULL)
    		return 0;
    	else if(root->left==NULL&&root->right==NULL)
    		return 0;
    	else if (root->left&&root->right)
    		temp=getlevel(root->left)+getlevel(root->right);
    	else if(root->left)
    		temp=getlevel(root->left);
    	else if(root->right)
    		temp=getlevel(root->right);
    	
    	if (temp>m)
    		m=temp;
    	diameterOfBinaryTree(root->left);
    	diameterOfBinaryTree(root->right);
    	return m;
        
    }
    int getlevel(TreeNode* tmp){
    	if (tmp==NULL)
    		return 0;
    	if(tmp->left==NULL&&tmp->right==NULL)
    		return 1;
    	else
    		return 1+max(getlevel(tmp->left),getlevel(tmp->right));
	}
	int max(int a,int b){
		return a>b?a:b;
	}
};
