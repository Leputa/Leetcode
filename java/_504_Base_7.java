import java.util.ArrayList;

public  class _504_Base_7 {
	 public _504_Base_7() {
		// TODO Auto-generated constructor stub
	}
	 public  String convertToBase7(int num) {
	        ArrayList<String>tmp=new ArrayList<>();
	        boolean tag=true;
	        if (num==0)
	        	return "0";
	        if(num<0) {
	        	tmp.add("-");
	        	tag=false;
	        	num=Math.abs(num);
	        }
	        while(num!=0) {
	        	tmp.add(String.valueOf(num%7));
	        	num/=7;
	        }
	        char []tmp2=new char[tmp.size()];
	        if (tag==false) {
	        	tmp2[0]='-';
	        	int i=tmp.size()-1;
	        	int flag=0;
	 	        for (String a:tmp) {
	 	        	if(flag==0) {
	 	        		flag=1;
	 	        		continue;
	 	        	}
	 	        	tmp2[i]=a.charAt(0);
	 	        	i--;
	 	        	if (i==0)
	 	        		break;
	 	        }
	        }
	        else {
	        	int i=tmp.size()-1;
	        	for (String a:tmp) {
	 	        	tmp2[i]=a.charAt(0);
	 	        	i--;
	 	        }
	        }
	        String ans=new String();
	        ans=String.valueOf(tmp2);
	        return ans;
	    }
}
