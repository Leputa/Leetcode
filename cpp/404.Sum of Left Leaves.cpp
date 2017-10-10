#include <iostream>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
    	int sum=0;
    	if(root==NULL)
    		return sum;
    	stack<TreeNode *>s;
    	TreeNode *tmp=root;
    	while(tmp||!s.empty()){
			while(tmp){
				s.push(tmp);
				tmp=tmp->left;
			}
			tmp=s.top();
			s.pop();
			sum+=tmp->val; 
			tmp=tmp->right;   		
		}
        return sum;
    }
};
