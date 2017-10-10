import java.util.LinkedList;
import java.util.Queue;


public class _225_Implement_Stack_using_Queues {
		
	 private Queue<Integer>queue1;
	 private Queue<Integer>queue2;
	
	 public _225_Implement_Stack_using_Queues() {
		 	queue1=new LinkedList<>();
		 	queue2=new LinkedList<>();
	    }
	    
	    /** Push element x onto stack. */
	    public void push(int x) {
	    	queue1.add(x);
	    }
	    
	    /** Removes the element on top of the stack and returns that element. */
	    public int pop() {
	    	int length=0;
	        while(!queue1.isEmpty()) {
	        	queue2.add(queue1.poll());
	        	length++;
	        }
	        int tmp=0;
	        for(int i=0;i<length;i++) {
	        	if(i==length-1)
	        		tmp=queue2.poll();
	        	else {
	        		queue1.add(queue2.poll());
	        	}
	        }
	        return tmp;
	    }
	    
	    /** Get the top element. */
	    public int top() {
	    	int length=0;
	        while(!queue1.isEmpty()) {
	        	queue2.add(queue1.poll());
	        	length++;
	        }
	        int tmp=0;
	        for(int i=0;i<length;i++) {
	        	if(i==length-1)
	        		tmp=queue2.peek();
	        	queue1.add(queue2.poll());
	        }
	        return tmp;
	        
	    }
	    
	    /** Returns whether the stack is empty. */
	    public boolean empty() {
	    	return queue1.isEmpty();
	    }

}
