#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>ret;
        if (root == NULL)
            return ret;
        queue<TreeNode *>_queue;
        _queue.push(root);
        int flag = 0; // left to right
        while(!_queue.empty()){
            int length = _queue.size();
            vector<int>tmp_vec;
            for (int i=0; i<length; i++){
                TreeNode* node = _queue.front();
                _queue.pop();
                tmp_vec.push_back(node->val);
                if (node -> left != NULL)
                    _queue.push(node->left);
                if (node -> right != NULL)
                    _queue.push(node->right);
            }
            if (flag == 1)
                reverse(tmp_vec.begin(), tmp_vec.end());
            ret.push_back(tmp_vec);
            flag = (flag + 1) % 2;
        }
        return ret;
    }
};

