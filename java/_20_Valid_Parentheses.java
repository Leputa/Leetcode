import java.util.Stack;

public class _20_Valid_Parentheses {
	 public boolean isValid(String s) {
			if(s.length()==0)
				return true;
			if(s.length()%2==1)
				return false;
			Stack<String>stack=new Stack<>();
			if(s.charAt(0)==')'||s.charAt(0)==']'||s.charAt(0)=='}')
				return false;
			stack.push(s.substring(0, 1));
			for(int i=1;i<s.length();i++) {
				if(s.charAt(i)=='('||s.charAt(i)=='['||s.charAt(i)=='{') {
					stack.push(s.substring(i, i+1));
				}
				else {
					String tmp=stack.peek();
					if(tmp.equals("(")&&s.substring(i,i+1).equals(")"))
						stack.pop();
					else if(tmp.equals("[")&&s.substring(i,i+1).equals("]"))
						stack.pop();
					else if(tmp.equals("{")&&s.substring(i,i+1).equals("}"))
						stack.pop();
					else
						return false;
				}
			}
			if(stack.isEmpty())
				return true;
			return false;
	 }
}
