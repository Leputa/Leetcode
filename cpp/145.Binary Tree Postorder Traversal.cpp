//Definition for a binary tree node.
# include <stack>
# include <vector>
# include <stdlib.h>
# include <iostream>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
    TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        TreeNode *tmpNode = root;
        vector<int> ret;
        if (tmpNode == NULL)
        	return ret;
		TreeNode *preVisitNode = NULL;
        stack<TreeNode*> S;
        while(tmpNode!=NULL || !S.empty()){
        	while(tmpNode!=NULL){
        		S.push(tmpNode);
        		tmpNode = tmpNode->left;
			}
			if (!S.empty()){
				tmpNode = S.top();
				if (tmpNode->right==NULL || preVisitNode==tmpNode->right){
					ret.push_back(tmpNode->val);
					preVisitNode = tmpNode;
					tmpNode = NULL;
					S.pop();
				}
				else
					tmpNode = tmpNode->right;
			}
		}
		return ret;
    }
};

int main(){
	TreeNode *root =  new TreeNode(1);
	root->right =  new TreeNode(2);
	root->right->left = new TreeNode(3);
	Solution s = Solution();
	s.postorderTraversal(root);
}


