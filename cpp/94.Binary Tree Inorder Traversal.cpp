#include <vector>
#include <stack>
using namespace std;


 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
private:
    void dfs(TreeNode* root, vector<int> &ret){
        if (root==NULL)
            return;
        dfs(root->left, ret);
        ret.push_back(root->val);
        dfs(root->right, ret);
    }
public:
//    vector<int> inorderTraversal(TreeNode* root) {
//        vector<int> ret;
//        dfs(root, ret);
//        return ret;
//    }
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode *>_stack;
        vector<int>ret;
        TreeNode* tmpNode = root;
        while(!_stack.empty() || tmpNode != NULL){
            while(tmpNode != NULL){
                _stack.push(tmpNode);
                tmpNode = tmpNode -> left;
            }
            tmpNode = _stack.top();
            _stack.pop();
            ret.push_back(tmpNode -> val);
            tmpNode = tmpNode ->right;
        }
        return ret;
    }
};