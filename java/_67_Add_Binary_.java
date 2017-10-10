
/*public class _67_Add_Binary_ {
	public String addBinary(String a, String b) {
		long aa=Long.parseLong(a,2);
		long bb=Long.parseLong(b,2);
		
		long  ans=aa+bb;
		return Long.toBinaryString(ans);
    }
}*/

public class _67_Add_Binary_ {
	public String addBinary(String a, String b) {
		int size_a=a.length();
		int size_b=b.length();

		StringBuilder strBuilder=new StringBuilder(Math.max(size_a, size_b));
		strBuilder.setLength(Math.max(size_a, size_b));
		int dif=Math.abs(size_a-size_b);
		System.out.println(dif);
		
		int tag=0;
		if(size_a>=size_b) {
			for(int i=size_b-1;i>=0;i--) {
				System.out.println(a.charAt(i+dif));
				System.out.println(b.charAt(i));
				if(tag==0) {
					if(a.charAt(i+dif)=='0'&&b.charAt(i)=='0') {
						strBuilder.setCharAt(i+dif, '0');
					}
					else if((a.charAt(i+dif)=='0'&&b.charAt(i)=='1')||(a.charAt(i+dif)=='1'&&b.charAt(i)=='0')) {
						strBuilder.setCharAt(i+dif, '1');
					}
					else if(a.charAt(i+dif)=='1'&&b.charAt(i)=='1') {
						strBuilder.setCharAt(i+dif, '0');
						tag=1;
					}
				}
				else if(tag==1) {
					if(a.charAt(i+dif)=='0'&&b.charAt(i)=='0') {
						strBuilder.setCharAt(i+dif, '1');
						tag=0;
					}
					else if((a.charAt(i+dif)=='0'&&b.charAt(i)=='1')||(a.charAt(i+dif)=='1'&&b.charAt(i)=='0')) {
						strBuilder.setCharAt(i+dif, '0');
						tag=1;
					}
					else if(a.charAt(i)=='1'&&b.charAt(i)=='1') {
						strBuilder.setCharAt(i+dif, '1');
						tag=1;
					}
				}
			}
		}
		else {
			for(int i=size_a-1;i>=0;i--) {
				if(tag==0) {
					if(b.charAt(i+dif)=='0'&&a.charAt(i)=='0') {
						strBuilder.setCharAt(i+dif, '0');
					}
					else if((b.charAt(i+dif)=='0'&&a.charAt(i)=='1')||(b.charAt(i+dif)=='1'&&a.charAt(i)=='0')) {
						strBuilder.setCharAt(i+dif, '1');
					}
					else if(b.charAt(i+dif)=='1'&&a.charAt(i)=='1') {
						strBuilder.setCharAt(i+dif, '0');
						tag=1;
					}
				}
				else if(tag==1) {
					if(b.charAt(i+dif)=='0'&&a.charAt(i)=='0') {
						strBuilder.setCharAt(i+dif, '1');
						tag=0;
					}
					else if((b.charAt(i+dif)=='0'&&a.charAt(i)=='1')||(b.charAt(i+dif)=='1'&&a.charAt(i)=='0')) {
						strBuilder.setCharAt(i+dif, '0');
						tag=1;
					}
					else if(b.charAt(i)=='1'&&a.charAt(i)=='1') {
						strBuilder.setCharAt(i+dif, '1');
						tag=1;
					}
				}
			}
			
		}
		
		
		if(size_a>=size_b) {
			for(int i=dif-1;i>=0;i--) {
				if(tag==0) {
					strBuilder.setCharAt(i, a.charAt(i));
				}
				if(tag==1) {
					if(a.charAt(i)=='0') {
						strBuilder.setCharAt(i, '1');
						tag=0;
					}
					else {
						strBuilder.setCharAt(i, '0');
						tag=1;
					}
				}
			}
		}
		else {
			for(int i=dif-1;i>=0;i--) {
				if(tag==0) {
					strBuilder.setCharAt(i, b.charAt(i));
				}
				if(tag==1) {
					if(b.charAt(i)=='0') {
						strBuilder.setCharAt(i, '1');
						tag=0;
					}
					else {
						strBuilder.setCharAt(i, '0');
						tag=1;
					}
				}
			}
		}
		
		if(tag==1) {
			StringBuilder tmp=new StringBuilder(strBuilder.length()+1);
			tmp.setLength(strBuilder.length()+1);
			tmp.setCharAt(0, '1');
			for(int i=0;i<strBuilder.length();i++)
				tmp.setCharAt(i+1,strBuilder.charAt(i));
			return tmp.toString();
		}
		return strBuilder.toString();	
    }
}
