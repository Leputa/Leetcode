import java.util.Stack;

public class _394_Decode_String {
    public String decodeString(String s) {
        String ans="";
        Stack<Integer>stack=new Stack<Integer>(); //ÖØ¸´´ÎÊý
        Stack<String>stack2=new Stack<String>();  //×Ö·û
        
        for (int i=0;i<s.length();i++){
        	if (s.charAt(i)>='0'&&s.charAt(i)<='9'){
        		int value=0;
        		while(s.charAt(i)>='0'&&s.charAt(i)<='9'){
        			value=value*10+Integer.valueOf(s.charAt(i)-'0');
        			i++;
        		}
        		stack.push(value);
        	}
        	if (s.charAt(i)=='['){
        		stack2.push(ans);
        		ans="";
        	}
        	else if (s.charAt(i)==']'){
        		StringBuilder tmpSB=new StringBuilder(stack2.pop());
        		int num=stack.pop();
        		for (int j=0;j<num;j++)
        			tmpSB.append(ans);
        		ans=tmpSB.toString();
        	}
        	else{
        		ans+=s.charAt(i);
        	}
        }
        return ans;
    }
}
