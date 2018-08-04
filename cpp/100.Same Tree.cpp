//Definition for a binary tree node.
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p==NULL && q==NULL)
        	return True;
        else if (p==NULL)
        	return False;
        else if (q==NULL)
        	return False;
        else if (p->val != q->val)
        	return False;
        else:
        	return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
