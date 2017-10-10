import java.util.HashMap;
import java.util.Iterator;
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
public class _513_Find_Bottom_Left_Tree_Value {
	public int findBottomLeftValue(TreeNode root) {
		TreeNode tmp=root;
		TreeNode cnt=null;
		int length=0;
		HashMap<Integer, Integer>map=new HashMap<>();
		Stack<TreeNode>stack=new Stack<>();
		Stack<Integer>tag=new Stack<>();
		while(tmp!=null || !stack.isEmpty()) {
			while(tmp!=null) {
				cnt=tmp;
				stack.push(tmp);
				
				//System.out.println(stack.size()+"  "+tmp.val);
				tag.push(0);
				tmp=tmp.left;
			}
			if (tag.peek()==1) {
				length=stack.size();
				//System.out.println(length+"   "+cnt.val);
				if(map.getOrDefault(length, null)==null) {
					map.put(length, cnt.val);
				}
				stack.pop();
				tag.pop();
				tmp=null;
			}
			else {
				tmp=stack.peek();
				tmp=tmp.right;
				tag.pop();
				tag.push(1);
			}
		}
		Iterator<Integer>it=map.keySet().iterator();
		int max=Integer.MIN_VALUE;
		while(it.hasNext()) {
			int temp=it.next();
			if(temp>max)
				max=temp;
		}
		//System.out.println(max);
		return map.get(max);
    }
}
