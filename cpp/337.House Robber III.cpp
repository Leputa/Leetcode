# include <vector>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
class Solution {
public:
    int rob(TreeNode* root) {
        vector<int>ans = dfs(root);
        return max(ans[0], ans[1]);
    }

private:
	vector<int>dfs(TreeNode * node){
		if (node == NULL){
            vector <int>tmp(2, 0);
			return tmp;
		}
		vector<int>left = dfs(node->left);
		vector<int>right = dfs(node->right);
		vector<int>ans(2, 0);
		ans[0] = left[1] + right[1] + node->val;
		ans[1] = max(left[0], left[1]) + max(right[0], right[1]);
		return ans;
	}
};
