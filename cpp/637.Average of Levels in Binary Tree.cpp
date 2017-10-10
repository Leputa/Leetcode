#include <vector>
#include <queue>
using namespace std;

Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
 
 
 
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        int count=0;
        double sum=0.0;
        queue<TreeNode*>Q;
        Q.push(root);
        Q.push(nullptr);      //nullptr as a partition for every level 
        while(!Q.empty()){
        	TreeNode *temp=Q.front();
        	Q.pop();    
			if(temp==nullptr){
				ans.push_back(sum/count);
				count=0;
				sum=0.0;
				if(!Q.empty())
					Q.push(nullptr);
			}
			else{
				sum+=temp->val;
				count++;
				if(temp->left)
					Q.push(temp->left);
				if(temp->right)
					Q.push(temp->right);
			}             
		}
        return ans;
    }
};
