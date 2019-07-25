#include <stack>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class BSTIterator {
private:
    stack<TreeNode*>_stack;
public:
    BSTIterator(TreeNode* root) {
        while(root != NULL){
            _stack.push(root);
            root = root -> left;
        }
    }
    /** @return the next smallest number */
    int next() {
        TreeNode *tmpNode = _stack.top();
        _stack.pop();
        tmpNode = tmpNode -> right;
        while(tmpNode != NULL){
            _stack.push(tmpNode);
            tmpNode = tmpNode -> left;
        }
    }
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !_stack.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */