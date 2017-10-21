import java.util.ArrayList;
import java.util.List;
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
public class _144_Binary_Tree_Preorder_Traversal {
	public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer>ans=new ArrayList<>();
        TreeNode tmp=root;
        Stack<TreeNode>stack=new Stack<>();
        while(tmp!=null||!stack.isEmpty()) {
        	while(tmp!=null) {
        		ans.add(tmp.val);
        		stack.push(tmp);
        		tmp=tmp.left;
        	}
        	if(!stack.isEmpty()) {
        		tmp=stack.pop();
        		tmp=tmp.right;
        	}
        }
        return ans;
    }
}
