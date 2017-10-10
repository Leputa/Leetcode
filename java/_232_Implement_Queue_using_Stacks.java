import java.util.Stack;

public class _232_Implement_Queue_using_Stacks {
	 /** Initialize your data structure here. */
	private Stack<Integer>stack1;
	private Stack<Integer>stack2;
    public _232_Implement_Queue_using_Stacks() {
    	stack1=new Stack<>();
    	stack2=new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
    	stack1.push(x);
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
    	if(stack1.isEmpty())
    		return -1;
    	while(!stack1.isEmpty()) {
    		stack2.push(stack1.pop());
    	}
    	int ans=stack2.pop();
    	while(!stack2.isEmpty()) {
    		stack1.push(stack2.pop());
    	}
        return ans;
    }
    
    /** Get the front element. */
    public int peek() {
    	if(stack1.isEmpty())
    		return -1;
    	while(!stack1.isEmpty()) {
    		stack2.push(stack1.pop());
    	}
    	int ans=stack2.peek();
    	while(!stack2.isEmpty()) {
    		stack1.push(stack2.pop());
    	}
        return ans;  
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack1.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
