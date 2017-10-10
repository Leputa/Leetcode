/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
public class _101_Symmetric_Tree {
	 public boolean isSymmetric(TreeNode root) {
		 if (root==null)
			 return true;
		 if (root.left==null&&root.right==null)
			 return true;
		 if (root.left==null&&root.right!=null)
			 return false;
		 TreeNode tmp1=root.left;
		 TreeNode tmp2=root.right;
		 tmp2=reverseTree(tmp2);
		 return isequal(tmp1,tmp2);
	 }

	private boolean isequal(TreeNode tmp1, TreeNode tmp2) {
		// TODO Auto-generated method stub
		if(tmp1==null&&tmp2==null)
			return true;
		if(tmp1==null&&tmp2!=null)
			return false;
		if(tmp1!=null&&tmp2==null)
			return false;
		if(tmp1.val!=tmp2.val)
			return false;
		return isequal(tmp1.left, tmp2.left) && isequal(tmp1.right, tmp2.right);
	}

	private TreeNode reverseTree(TreeNode tmp2) {
		// TODO Auto-generated method stub
		if(tmp2==null)
			return tmp2;
		TreeNode t1=tmp2.left;
		tmp2.left=tmp2.right;
		tmp2.right=t1;
		if(tmp2.left!=null)
			reverseTree(tmp2.left);
		if(tmp2.right!=null)
			reverseTree(tmp2.right);
		return tmp2;
	}
}
