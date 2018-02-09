
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class _102_Binary_Tree_Level_Order_Traversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
       List<List<Integer>>ans=new ArrayList<List<Integer>>();
       if (root==null)
    	   return ans;
       Queue<TreeNode>queue=new LinkedList<>();
       TreeNode tmp=root;
       queue.add(tmp);
       while(!queue.isEmpty()){
    	   int length=queue.size();
    	   List<Integer>tmpList=new ArrayList<>();
    	   for (int i=0;i<length;i++){
    		   tmp=queue.poll();
    		   tmpList.add(tmp.val);
    		   if(tmp.left!=null)
    			   queue.add(tmp.left);
    		   if(tmp.right!=null)
    			   queue.add(tmp.right);
    	   }
    	   ans.add(tmpList);
       }
       return ans;	
    }
}
