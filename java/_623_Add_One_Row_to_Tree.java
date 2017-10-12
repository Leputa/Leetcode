import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class _623_Add_One_Row_to_Tree {
    public TreeNode addOneRow(TreeNode root, int v, int d) {
    	if(d==1) {
    		TreeNode newNode=new TreeNode(v);
    		newNode.left=root;
    		return newNode;
    	}
    	Queue<TreeNode>queue=new LinkedList<>();
    	TreeNode tmp=root;
    	queue.add(tmp);
    	int level=1;
    	List<TreeNode>list=new ArrayList<>(); //¼ÇÂ¼d-1²ã
    	while(!queue.isEmpty()) {
    		int len=queue.size();
    		level++;
    		if(level==d) {
    			while(len>0) {
    				tmp=queue.poll();
    				list.add(tmp);
    				len--;
    			}
    			break;
    		}
    		while(len>0) {
    			tmp=queue.poll();
    			if(tmp.left!=null)
    				queue.add(tmp.left);
    			if(tmp.right!=null)
    				queue.add(tmp.left);
    			len--;
    		}
    	}
    	for (TreeNode node:list) {
    		TreeNode newNodeLeft=new TreeNode(v);
    		TreeNode newNodeRight=new TreeNode(v);
    		TreeNode leftNode=node.left;
    		TreeNode rightNode=node.right;
    		node.left=newNodeLeft;
    		node.right=newNodeRight;
    		newNodeLeft.left=leftNode;
    		newNodeRight.right=rightNode;
    	}
    	return root;
    }
}
