import java.util.ArrayList;

public class _155_Min_Stack {
	 /** initialize your data structure here. */
	private int min;
	private ArrayList<Integer>stack;
    public _155_Min_Stack() {
    	stack=new ArrayList<Integer>();
    	min=Integer.MAX_VALUE;
        
    }
    
    public void push(int x) {
    	if(x<min)
    		min=x;
    	stack.add(x);
    }
    
    public void pop() {
    	int len=stack.size();
    	if(stack.get(len-1)==min) {
    		min=Integer.MAX_VALUE;
    		for(int i=0;i<len-1;i++)
    			if(stack.get(i)<min)
    				min=stack.get(i);
    	}
        stack.remove(len-1);
    }
    
    public int top() {
    	return stack.get(stack.size()-1);
        
    }
    
    public int getMin() {
        return min;
    }

}
