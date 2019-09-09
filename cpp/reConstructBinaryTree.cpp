
#include <vector>
#include <algorithm>
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
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        if (pre.size() == 0)
            return nullptr;
        if (pre.size() == 1)
            return new TreeNode(pre[0]);
        TreeNode* root = new TreeNode(pre[0]);
        unsigned long mid_idx = -1;
        for (unsigned long i=0; i<vin.size(); i++){
            if (vin[i] == pre[0]){
                mid_idx = i;
                break;
            }
        }
        vector<int>left_pre(pre.begin()+1, pre.begin()+mid_idx+1);
        vector<int>left_vin(vin.begin(), vin.begin()+mid_idx);
        root -> left = reConstructBinaryTree(left_pre, left_vin);
        vector<int>right_pre(pre.begin()+mid_idx+1, pre.end());
        vector<int>right_vin(vin.begin()+mid_idx+1, vin.end());
        root -> right = reConstructBinaryTree(right_pre, right_vin);
        return root;
    }
};