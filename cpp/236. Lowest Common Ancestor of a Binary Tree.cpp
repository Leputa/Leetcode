#include <vector>
using namespace std;

// Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
private:
    vector<TreeNode*>stack_p;
    vector<TreeNode*>stack_q;
    bool get_path(vector<TreeNode*>&stack, TreeNode *root, TreeNode* node){
        stack.push_back(root);
        if (root == node)
            return true;
        bool is_path = false;
        if (root->left != NULL)
            is_path = get_path(stack, root->left, node);
        if (!is_path && root->right != NULL)
            is_path = get_path(stack, root->right, node);
        if (!is_path)
            stack.pop_back();
        return is_path;
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        get_path(stack_p, root, p);
        get_path(stack_q, root, q);
        int end_idx = min(stack_q.size(), stack_p.size())-1;
        while(stack_p[end_idx] != stack_q[end_idx])
            end_idx--;
        return stack_p[end_idx];
    }
};
