#include <stack>
using namespace std;

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};
class Solution {
/*
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
*/
private:
    TreeNode *preNode;
    TreeNode *listhead;

void ConvertNode(TreeNode* pRootOfTree){
    {
        if (pRootOfTree == nullptr) return;
        ConvertNode(pRootOfTree->left);    // 左
        if (preNode == nullptr){           // 中
            preNode = pRootOfTree;
            listhead = pRootOfTree;
        }
        else{
            preNode -> right = pRootOfTree;
            pRootOfTree -> left = preNode;
            preNode = pRootOfTree;
        }
        ConvertNode(pRootOfTree->right);
    }
} 
public:
    TreeNode* Convert(TreeNode* pRootOfTree){
        if (pRootOfTree == nullptr)
            return nullptr;
        preNode = nullptr;
        ConvertNode(pRootOfTree);
        return listhead;
    }
};