#include <stdio.h>
#include <string>
#include <sstream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};



string num2str(int i)
{
        stringstream ss;
        ss<<i;
        return ss.str();
}

class Solution {
public:
    string tree2str(TreeNode* t) {
        if (t==NULL)
        	return "";
        string ans=num2str(t->val);
        
        if(t->left)
        	ans+="("+tree2str(t->left)+")";   	 
        if(t->right&&t->left!=NULL)
        	ans+="("+tree2str(t->right)+")";
    	
        if(t->right&&t->left==NULL)
            ans+="()("+tree2str(t->right)+")";
        
        return ans;
    }
};
