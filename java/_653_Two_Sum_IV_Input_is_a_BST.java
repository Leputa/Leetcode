
import java.util.ArrayList;
import java.util.Stack;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class _653_Two_Sum_IV_Input_is_a_BST {
	public boolean findTarget(TreeNode root, int k) {
		if (root ==null)
			return false;
		ArrayList<Integer> list=new ArrayList<>();
		TreeNode tmp=root;
		Stack<TreeNode> stack=new Stack<>();
		while(tmp!=null||!stack.isEmpty()) {
			while(tmp!=null) {
				stack.push(tmp);
				tmp=tmp.left;
			}
			if(!stack.isEmpty()) {
				tmp=stack.pop();
				list.add(tmp.val);
				tmp=tmp.right;
			}
		}
		int len=list.size();
		if(list.get(0)*2>k)
			return false;
		if(list.get(len-1)*2<k)
			return false;
		int i=0;
		int j=len-1;
		while(i<j) {
			if (list.get(i)+list.get(j)==k)
				return true;
			else if (list.get(i)+list.get(j)<k)
				i++;
			else if (list.get(i)+list.get(j)>k)
				j--;
		}
		return false;
    }
}
