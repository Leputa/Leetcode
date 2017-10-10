#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
    	if(s==t)
    		return true;
    	if(s==NULL&&t==NULL)
    		return true;
    	if(s!=NULL&&t==NULL)
    		return false;
    	if(s==NULL&&t!=NULL)
    		return false;
    	if(isequal(s,t))
    		return true;
    	else
    		return(isSubtree(s->left, t)||isSubtree(s->right, t));
    	return false;
    }
    bool isequal(TreeNode* s, TreeNode* t){
    	if(s==NULL&&t==NULL)
    		return true;
    	if(s!=NULL&&t==NULL)
    		return false;
    	if(s==NULL&&t!=NULL)
    		return false;
    	if(s->val!=t->val)
    		return false;
    	return (isequal(s->left,t->left)&&isequal(s->right,t->right));
	}
};
