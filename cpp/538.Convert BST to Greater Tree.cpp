#include <stack>
#include <stdio.h>
#include <malloc.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

struct Node{
	int val;
	Node *next;
};

Node *head=(Node*)malloc(sizeof(Node));
 
class Solution {
public:	    

	void CreatList(TreeNode* root){
    	if (root==NULL)
    		return;
    	stack<TreeNode*> S;
    	TreeNode *tmp=root;
    	head->val=root->val;
    	head->next=NULL;
        Node *tmpNode=head;
    	while(tmp||!S.empty()){
			while(tmp){
				S.push(tmp);
				if(tmp!=root){
					Node*tmpNode2=(Node*)malloc(sizeof(Node));
					tmpNode2->val=tmp->val;
					tmpNode->next=tmpNode2;
					tmpNode2->next=NULL;
					tmpNode=tmpNode2;
				}
				tmp=tmp->left;	
			}
			tmp=S.top();
			S.pop();	
            tmp=tmp->right;
		}
	}
	
	void updataTree(TreeNode* root){
		if (root==NULL)
    		return;
    	stack<TreeNode*> S;
    	TreeNode *tmp=root;
    	while(tmp||!S.empty()){
			while(tmp){
				S.push(tmp);
				int data=tmp->val;
				Node*tmpNode=head;
				while(tmpNode!=NULL){
					if(tmpNode->val>data)
						tmp->val+=tmpNode->val;
                    tmpNode=tmpNode->next;
				}
				tmp=tmp->left;	
			}
			tmp=S.top();
			S.pop();	
            tmp=tmp->right;
		}
	}
    TreeNode* convertBST(TreeNode* root) {
        CreatList(root);
        updataTree(root);
        return root;
    }
};



