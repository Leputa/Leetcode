import java.util.Stack;

public class _503_Next_Greater_Element_II {
	public int[] nextGreaterElements(int[] nums) {
		int length=nums.length;
		int[]ans=new int[length];
		
		int[]copy=new int[length*2];
		for(int i=0;i<length;i++) {
			copy[i]=nums[i];
			ans[i]=-1;
		}
		for(int i=length;i<length*2;i++)
			copy[i]=nums[i-length];
		
		Stack<Integer>stack=new Stack<>();
		for (int i=0;i<2*length;i++) {
			if(stack.isEmpty())
				stack.push(i);
			else {
				int index=stack.peek();
				while(!stack.isEmpty()&&copy[index]<copy[i]) {
					if(index>=length)
						index-=length;
					ans[index]=copy[i];
					stack.pop();
                    if(!stack.isEmpty())
                        index=stack.peek();
				}
                stack.push(i);
			}
		}
		return ans;
    }
}
