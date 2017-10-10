
public class _551_Student_Attendance_Record_I {
	public boolean checkRecord(String s) {
        int cntA=0;
        int cntL=0;
        boolean tag=false;
        for (int i=0;i<s.length();i++) {
        	if(s.charAt(i)=='A') {
        		cntA++;
        		cntL=0;
        	} 
        	if(s.charAt(i)=='P')
        		cntL=0;
        	if(!(tag))
        		if(s.charAt(i)=='L') {
        			cntL++;
        			if(cntL>=3)
        				tag=true;
        		}
        			
        }
        if (cntA>1||tag)
        	return false;
        return true;  
    }
}
