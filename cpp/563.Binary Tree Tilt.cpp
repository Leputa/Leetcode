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
    int findTilt(TreeNode* root) {
    	int sum=0;
    	if(root==NULL)
    		return sum;
    	TreeNode *tmp=root;
    	stack<TreeNode*> s;
    	while(tmp||!s.empty()){
    		while(tmp){
    			s.push(tmp);
    			tmp=tmp->left;	
			}
			if(!s.empty()){
				tmp=s.top();
				sum+=abs(getSubtreesum(tmp->left)-getSubtreesum(tmp->right));
				s.pop();
				tmp=tmp->right;
			}	
		}
    	return sum;
    }
    
    int getSubtreesum(TreeNode *tmp){
    	int sum=0;
    	if(tmp==NULL)
    		return sum;
    	stack<TreeNode*> s;
    	while(tmp||!s.empty()){
    		while(tmp){
    			s.push(tmp);
    			tmp=tmp->left;	
			}
			if(!s.empty()){
				tmp=s.top();
				sum+=tmp->val;
				s.pop();
				tmp=tmp->right;
			}	
		}
		return sum;	
	}
};
